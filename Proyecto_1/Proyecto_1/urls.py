"""Proyecto_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from Proyecto_1.views import hola, fecha_actual, vista_con_template, \
    saludo_desde_template,indice


urlpatterns = [
    path('admin/', admin.site.urls),
    path("holanda/", hola),
    path("fecha/", fecha_actual),
    path("vista-con-template/", vista_con_template),
    path("saludo-desde-template/", saludo_desde_template),
    path("",indice, name="indice"),

    path("products/", include("products.urls")),
]
