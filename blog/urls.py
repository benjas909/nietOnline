from django.urls import path
from . import views
from . models import Iconos

icons = Iconos.objects.all()

urlpatterns = [
    path("", views.inicio, name="page-home"),
    path("info/", views.about, name="page-info"),
    path("Facebook/", views.facebook, name="Facebook"),
    path("Youtube/", views.youtube, name="YouTube"),
    path("Instagram/", views.instagram, name="Instagram"),
    path("Netflix/", views.netflix, name="Netflix"),
    path("Spotify/", views.spotify, name="Spotify"),
    path("search/<str:search>/", views.searchPage)
]
'''
for item in icons:
    itemName=str(item)
    urlpatterns.append(path("search/<str:"+itemName+"/", views.tutorialPage, name="page-tuto-"+itemName))
'''