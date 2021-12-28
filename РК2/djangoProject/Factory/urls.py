from django.urls import path

from . import views

urlpatterns = [
path('', views.index),
path('Manufacturer/', views.manufacturers),
path('Detail/', views.details),
path('Manufacturer/<int:id>/', views.manufacturer),
path('Program/<int:id>/', views.detail),
]