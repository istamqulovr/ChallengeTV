from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = "'index"),
    path('challenges/',views.challenge_tv),
    path('challenges/<slug>/', views.workout,name="workout")
]