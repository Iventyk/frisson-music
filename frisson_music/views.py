from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    TemplateView,
    CreateView
)

from .forms import AlbumUpdateForm, CustomUserCreationForm, UserUpdateForm
from .models import Album, User


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


class AlbumUpdateView(UpdateView):
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
