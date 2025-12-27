from collections import defaultdict
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    TemplateView,
    CreateView,
)

from .forms import (
    AlbumUpdateForm,
    CustomUserCreationForm,
    UserUpdateForm,
    CommentForm,
    RatingForm,
)
from .models import Album, User, Rating, Comment


class HomePageView(TemplateView):
    template_name = "frisson_music/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest = {}
        for media_type in ["ANIME", "SERIES", "GAME", "MOVIE"]:
            latest[media_type] = Album.objects.latest_by_type(media_type)
        context["latest"] = latest
        return context


class AlbumListView(ListView):
    model = Album
    context_object_name = "albums"
    ordering = ["-release_date"]
    paginate_by = 32

    def get_queryset(self):
        qs = super().get_queryset()
        album_type = self.kwargs.get("album_type")
        search = self.request.GET.get("search")
        if album_type:
            qs = qs.filter(media_type=album_type)
        if search:
            qs = qs.filter(album_title__icontains=search)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query_params = self.request.GET.copy()
        query_params.pop("page", None)
        context["query_params"] = query_params.urlencode()
        return context


class AlbumDetailView(DetailView):
    model = Album
    context_object_name = "album"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album = self.object

        # --- Comments ---
        context["comments"] = album.comments.select_related("user").order_by(
            "-created_at"
        )
        context["comment_form"] = CommentForm()

        # --- Rating: Average ---
        context["average_rating"] = round(album.average_rating(), 1)

        # --- User's Rating ---
        if self.request.user.is_authenticated:
            context["user_rating"] = album.ratings.filter(
                user=self.request.user
            ).first()
        else:
            context["user_rating"] = None

        context["stars"] = [1, 2, 3, 4, 5]
        context["rating_form"] = RatingForm()
        return context

    def post(self, request, *args, **kwargs):
        album = self.get_object()
        redirect_response = redirect("album-detail", pk=album.pk)

        # --- Comment submission ---
        if "text" in request.POST and request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.album = album
                comment.user = request.user
                comment.save()
            return redirect_response

        # --- Rating submission ---
        if "score" in request.POST and request.user.is_authenticated:
            score = int(request.POST.get("score", 0))
            if 1 <= score <= 5:
                Rating.objects.update_or_create(
                    album=album, user=request.user, defaults={"score": score}
                )
            return redirect_response

        return redirect_response


class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = Album
    form_class = AlbumUpdateForm

    def get_success_url(self):
        return reverse_lazy("album-detail", kwargs={"pk": self.object.pk})


class MediaListView(ListView):
    template_name = "frisson_music/media_list.html"
    context_object_name = "media_list"
    paginate_by = 15

    def get_queryset(self):
        return (
            Album.objects.exclude(media_title__isnull=True)
            .exclude(media_title="")
            .order_by("media_title")
            .values("media_title", "media_type")
            .distinct()
        )


class MediaDetailView(ListView):
    model = Album
    template_name = "frisson_music/media_detail.html"
    context_object_name = "albums"

    def get_queryset(self):
        media_title = self.kwargs.get("media_title")
        media_type = self.request.GET.get("type")
        return Album.objects.by_media_title(
            media_title, media_type
        ).select_related()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        albums = context["albums"]
        grouped = defaultdict(list)
        for album in albums:
            grouped[album.part_or_season].append(album)
        context["grouped_albums"] = dict(sorted(grouped.items()))
        context["media_title"] = self.kwargs.get("media_title")
        context["media_type"] = self.request.GET.get("type")
        return context


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("rules")


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "registration/profile_edit.html"
    success_url = reverse_lazy("home")

    def get_object(self, queryset=None):
        return self.request.user


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user == request.user:
        album_id = comment.album.id
        comment.delete()
        return redirect("album-detail", pk=album_id)
    return redirect("album-detail", pk=comment.album.id)
