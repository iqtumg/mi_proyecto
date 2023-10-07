from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def inicio(request):
    return HttpResponse("<h1>BIENVENIDO<h1>")


def curdp(request):
    return render(request, "pagina/personal1.html")


def buses1(request):
    return render(request, "pagina/buses.html")


def calendario(request):
    return render(request, "pagina/calendario.html")


def horarios(request):
    return render(request, "pagina/horarios.html")
