from django.contrib import admin
from django.urls import path, include
from stock import views

urlpatterns = [
    path('all_stock/', views.stock),
]
