from django.urls import path
from . import views
from . models import Iconos

icons = Iconos.objects.all()

urlpatterns = [
    path("", views.inicio, name="page-home"),
    path("info/", views.about, name="page-info"),
    path("tutorial/<str:tutorial>/", views.tutorial, name="tutorial"),
    path("search/", views.searchPage, name="search-results")
]

# linea de quitada del home.html (barra de navegacion):
#  <!-- <li class="list-group-item list-group-item-light"><a href="{% url 'tutorial' %}">Nuevos tutoriales</a></li> -->