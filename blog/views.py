from django.shortcuts import render
from django.http import HttpResponse
from .models import Iconos


posts = [
    {
        "titulo": "Bienvenidos a NietOnline!",
        "autor": "NERV1_DEV",
        "contenido": "Esta página busca ayudar a personas de tercera edad a aprender a usar las aplicaciones modernas.",
        "fecha": "7/11/2021",
    },
    {
        "titulo": "¿Quiénes Conforman el grupo?",
        "autor": "NERV1_DEV",
        "contenido": "El grupo está conformado por Alexander Inostroza, Felipe Zambrano, Gonzalo Alarcón y Benjamín Aguilera.",
        "fecha": "8/11/2021",
    },
]


def inicio(request):
    icons = Iconos.objects.all()
    context = {"icons":icons}
    return render(request, "blog/home.html", context)


def about(request):
    context = {"posts": posts}
    return render(request, "blog/about.html", context)

