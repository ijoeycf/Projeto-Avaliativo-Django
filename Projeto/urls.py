"""
URL configuration for Projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from core.views import (
    home,
    agendamentos,
    cadastraAgendamento,
    editaAgendamento,
    excluiAgendamento,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('agendamentos', agendamentos, name='agendamentos'),
    path('formulario', cadastraAgendamento, name='formulario'),
    path('agendamentos/<int:id>/editar', editaAgendamento, name='editaAgendamento'),
    path('agendamentos/<int:id>/excluir', excluiAgendamento, name='excluiAgendamento'),
]
