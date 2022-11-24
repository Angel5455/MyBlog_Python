from django.urls import path

#VIEWS
from . import views

urlpatterns = [
    path('', views.perfil, name='perfil'),
]