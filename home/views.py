from django.shortcuts import render
from django.http import HttpResponse 

def home(request):
    return render(request, 'body.html')

def contacto(request):
    return render(request, 'contacto.html')

def datos(request):
    return render(request, 'datos_historicos.html')

def estaciones(request):
    return render(request, 'estaciones.html')

def pronostico(request):
    return render(request, 'pronostico_mp10.html')

