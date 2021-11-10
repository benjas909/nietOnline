from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="page-home"),
    path("info/", views.about, name="page-info"),
]
