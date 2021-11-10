from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse('<h1>El benja es puto</h.1>')

