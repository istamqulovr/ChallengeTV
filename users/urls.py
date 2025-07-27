from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('registration/',views.login,name='registration'),
    path('login/',views.login,name="login"),
    path('profile/',views.profile_view,name="profile"),
    path('logout/', views.logout_view, name='logout')

]

