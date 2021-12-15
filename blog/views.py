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
        "titulo": "¿Quiénes conforman NERV1_DEV?",
        "autor": "NERV1_DEV",
        "contenido": "NERV1_DEV está conformado por Alexander Inostroza, Felipe Zambrano, Gonzalo Alarcón y Benjamín Aguilera.",
    },
]


class simple_tuple:
    def __init__(self, firstElement, secondElement):
        self.firstElement = firstElement
        self.secondElement = secondElement


def inicio(request):
    icons = Iconos.objects.all()
    i = 1.5
    iconList = []
    interval = 0.1
    for icon in icons:
        iconList.append(simple_tuple(icon, str(i)))
        i += interval
    context = {"icons": iconList}
    return render(request, "blog/home.html", context)


def about(request):
    context = {"posts": posts}
    return render(request, "blog/about.html", context)


def searchPage(request):
    search = request.GET["q"]
    tags = [tag for tag in Tag.objects.all() if tag.name.lower() in search.lower()]
    tutorials = Tutorial.objects.filter(tags__in = tags).distinct()
    related_tags = Tag.objects.filter(tutorial__in  = tutorials).distinct()
    i=1
    interval = 0.1
    tutorials_list =[]
    for tutorial in tutorials:
        tutorials_list.append(simple_tuple(tutorial, str(i)))
        i += interval
    context = {"search": search, "tutorialsList": tutorials_list, "tags": tags, "related": related_tags}
    return render(request, "blog/searchPage.html", context)
