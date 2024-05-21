from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='body'),
    path('datos_historicos.html', views.datos, name='datos'),
    path('estaciones.html', views.estaciones, name='estaciones'),
    path('pronostico_mp10.html', views.pronostico, name='pronostico'),
]