from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    TemplateView,
    CreateView
)

from .forms import (
    AlbumUpdateForm,
    CustomUserCreationForm,
    UserUpdateForm,
    CommentForm,
    RatingForm
)
from .models import Album, User, Rating


class HomePageView(TemplateView):
    template_name = "frisson_music/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["latest_anime"] = Album.objects.filter(
            media_type="ANIME"
        ).order_by('-release_date')[:5]
        context["latest_series"] = Album.objects.filter(
            media_type="SERIES"
        ).order_by('-release_date')[:5]
        context["latest_game"] = Album.objects.filter(
            media_type="GAME"
        ).order_by('-release_date')[:5]
        context["latest_movie"] = Album.objects.filter(
            media_type="MOVIE"
        ).order_by('-release_date')[:5]

        return context


class AlbumListView(ListView):
    model = Album
    context_object_name = "albums"
    ordering = ["-release_date"]
    paginate_by = 32

    def get_queryset(self):
        queryset = super().get_queryset()
        album_type = self.kwargs.get("album_type")

        if album_type:
            queryset = queryset.filter(media_type=album_type)

        return queryset


class AlbumDetailView(DetailView):
    model = Album
    context_object_name = "album"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Comments
        context["comments"] = self.object.comments.order_by("-created_at")
        context["comment_form"] = CommentForm()

        # Rating: Average
        ratings = self.object.ratings.all()
        if ratings.exists():
            avg = round(sum(r.score for r in ratings) / ratings.count(), 1)
        else:
            avg = 0
        context["average_rating"] = avg

        # User's Rating
        user_rating = None
        if self.request.user.is_authenticated:
            try:
                user_rating = Rating.objects.get(album=self.object,
                                                 user=self.request.user)
            except Rating.DoesNotExist:
                user_rating = None
        context["user_rating"] = user_rating

        # Stars for template
        context["stars"] = [1, 2, 3, 4, 5]

        # Rating form
        context["rating_form"] = RatingForm()

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        # Comment submission
        if "text" in request.POST:
            if not request.user.is_authenticated:
                return redirect("login")
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.album = self.object
                comment.user = request.user
                comment.save()
            return redirect("album-detail", pk=self.object.pk)

        # Rating submission
        if "score" in request.POST:
            if not request.user.is_authenticated:
                return redirect("login")
            rating_value = int(request.POST.get("score", 0))
            if 1 <= rating_value <= 5:
                Rating.objects.update_or_create(
                    album=self.object,
                    user=request.user,
                    defaults={"score": rating_value}
                )
            return redirect("album-detail", pk=self.object.pk)

        return redirect("album-detail", pk=self.object.pk)


class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = Album
    form_class = AlbumUpdateForm

    def get_success_url(self):
        return reverse("album-detail", kwargs={"pk": self.object.pk})


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "registration/profile_edit.html"
    success_url = reverse_lazy("home")

    def get_object(self, queryset=None):
        return self.request.user
