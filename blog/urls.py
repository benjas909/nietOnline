from django.urls import path
from . import views
from . models import Iconos

icons = Iconos.objects.all()

urlpatterns = [
    path("", views.inicio, name="page-home"),
    path("info/", views.about, name="page-info"),
    path("newtutorial/", views.nwtutorial, name="New-tutorial"),
    path("search/", views.searchPage, name="search-results")
]
