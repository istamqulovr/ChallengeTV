from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('join_challenge/', views.join_challenge, name='join_challenge'),


]
