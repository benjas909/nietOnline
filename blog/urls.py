from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="page-home"),
    path("info/", views.about, name="page-info"),
    path("Facebook/", views.facebook, name="Facebook"),
    path("Youtube/", views.youtube, name="YouTube"),
    path("Instagram/", views.instagram, name="Instagram"),
    path("Netflix/", views.netflix, name="Netflix"),
    path("Spotify/", views.spotify, name="Spotify"),
]
