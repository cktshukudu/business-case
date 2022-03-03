from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createTemplate/', views.createTemplate, name='createclear'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('update/', views.update, name='update'),
]
