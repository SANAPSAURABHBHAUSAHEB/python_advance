"""
URL configuration for home page.
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.greet),
    path('hello/', views.hello),
    path('bye/', views.bye),
    path('name/', views.name),
]
