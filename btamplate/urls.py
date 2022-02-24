from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('templates/create/', views.create, name='createclear'),
]