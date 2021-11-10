from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    return HttpResponse("<h1>chupalo zamquin buenas tardes</h1>")


def about(request):
    return HttpResponse("<h1>Sobre los pibes</h1>")
