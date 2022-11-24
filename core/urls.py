from django.urls import path

#VIEWS
from . import views

urlpatterns = [
    path('', views.index, name='home'),
]