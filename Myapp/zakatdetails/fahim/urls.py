from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.user_login, name='login'),
    path('signup', views.user_signup, name='signup'),
    path('logout', views.user_logout, name='logout'),
    path('home', views.home, name='home'),
  #  path('register', views.register, name = "register"),
    path('register', views.register, name='register'),
    path('madrasa', views.madrasa, name = "madrasa"),
    path('madrasadetails/<int:id>', views.madrasadetails, name='madrasadetails'),
    path('zakat_entry', views.process_zakat_entry, name='zakat_entry'),
]

