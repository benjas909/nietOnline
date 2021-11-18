from django.shortcuts import render
from django.http import HttpResponse
from .models import *


posts = [
    {
        "titulo": "Bienvenidos a NietOnline!",
        "autor": "NERV1_DEV",
        "contenido": "Esta página busca ayudar a personas de tercera edad a aprender a usar las aplicaciones modernas.",
    },
    {
        "titulo": "¿Quiénes Conforman el grupo?",
        "autor": "NERV1_DEV",
        "contenido": "El grupo está conformado por Alexander Inostroza, Felipe Zambrano, Gonzalo Alarcón y Benjamín Aguilera.",
    },
]


def inicio(request):
    icons = Iconos.objects.all()
    context = {"icons": icons}
    return render(request, "blog/home.html", context)


def about(request):
    context = {"posts": posts}
    return render(request, "blog/about.html", context)

def nwtutorial(request):
    return render(request, "blog/newtutorial.html")

def searchPage(request):
    search = request.GET["q"]
    tags = [tag for tag in Tag.objects.all() if tag.name.lower() == search.lower()]
    tutorials = Tutorial.objects.filter(tag__in=tags)
    #tags = Tag.objects.all()
    context = {"search" : search, "tutorialsList" : tutorials, "tags" : tags}
    return render(request, "blog/searchPage.html",context)