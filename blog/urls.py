from django.urls import path

#VIEWS
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('<int:id>', views.post, name='post'),

]