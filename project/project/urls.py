"""project URL Configuration

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
from django.urls import path
from app.views import ProgramacaoList, TipoEventoForm, EventoForm, PalestranteList, PalestranteEdit,PalestranteUpdate, PalestranteDelete, PalestranteForm, PalestranteAdd, LocalForm, LocalAdd, EventoAdd, EventoList, EventoDelete, EventoEdit, EventoUpdate, LocalList

urlpatterns = [
    path('admin/', admin.site.urls),
    #Formulários (exibição)
    path('cadastro/TipoEvento/', TipoEventoForm, name='TipoEventoForm'),
    path('cadastro/Evento/', EventoForm, name='EventoForm'),
    path('cadastro/Palestrante/', PalestranteForm, name='PalestranteForm'),
    path('cadastro/Local/', LocalForm, name='LocalForm'),
    #Formulários (inserções)
    path('cadastro/Evento/add/', EventoAdd, name='EventoAdd'),
    path('cadastro/Local/add/', LocalAdd, name='LocalAdd'),
    path('cadastro/Palestrante/add/', PalestranteAdd, name='PalestranteAdd'),
    #Formulários (exibição para edição)
    path('cadastro/Evento/<int:pk>', EventoEdit, name='EventoEdit'),
    path('cadastro/Palestrante/<int:pk>', PalestranteEdit, name='PalestranteEdit'),
    #Formulários (exclusões)
    path('cadastro/Evento/delete/<int:pk>', EventoDelete, name='EventoDelete'),
    path('cadastro/Palestrante/delete/<int:pk>', PalestranteDelete, name='PalestranteDelete'),
    #Formulários (edição)
    path('cadastro/Evento/update/<int:pk>', EventoUpdate, name='EventoUpdate'),
    path('cadastro/Palestrante/update/<int:pk>', PalestranteUpdate, name='PalestranteUpdate'),
    #Listagens
    path('Evento/', EventoList, name='EventoList'),
    path('Palestrante/', PalestranteList, name='PalestranteList'),
    path('Local/', LocalList, name='LocalList'),
    path('Programacao/', ProgramacaoList, name='ProgramacaoList'),
]
