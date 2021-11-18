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
'''
for item in icons:
    itemName=str(item)
    urlpatterns.append(path("search/<str:"+itemName+"/", views.tutorialPage, name="page-tuto-"+itemName))
'''