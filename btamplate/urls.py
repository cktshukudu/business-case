from django.urls import path
from . import views
from django.contrib.auth import views as auth_view



urlpatterns = [
    path('', views.index, name='index'),
    path('createTemplate/', views.createTemplate, name='createTemplate'),
    path('signup/', views.signup, name='signup'),
     path('login/', auth_view.LoginView.as_view(template_name='btamplate/login.html'), name="login"),
    path('update/', views.update, name='update'),
    path('about_us/', views.about_us, name='about_us'),
]
