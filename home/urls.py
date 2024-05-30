from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='body'),
    path('contacto.html', views.contacto, name='contacto'),
    path('datos_historicos.html', views.datos, name='datos'),
    path('estaciones.html', views.estaciones, name='estaciones'),
    path('pronostico_mp10.html', views.pronostico, name='pronostico'),
    path('proyecto.html', views.proyecto, name='proyecto'),
    path('mp10.html', views.mp10, name='mp10'),
    path('quienesomos.html', views.quienesomos, name='quienesomos'),
]