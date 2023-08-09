"""
URL configuration for textualsimilarity project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.bienvenida_pln, name='bienvenida_pln'),
    path('admin/', admin.site.urls),
    path('hola/', views.hola_mundo, name='hola_mundo'),
    path('similitud/', views.mostrar_tabla, name='mostrar_tabla'),  # Agrega esta línea
    path('dashboard/', views.dashboard, name='dashboard'),
    path('accounts/', include('allauth.urls')),
    path('guardar_contenido/', views.guardar_contenido, name='guardar_contenido'),
    path('hola_mundo_json/', views.hola_mundo_json, name='hola_mundo_json'),
    path('consumir_hola_mundo_json/', views.consumir_hola_mundo_json, name='consumir_hola_mundo_json'),
    path('recibirCorpus/',views.TextoSim, name='recibirCorpus'),
    path('api/', views.api_view, name='api'),
]
