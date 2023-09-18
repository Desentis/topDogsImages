from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('127.0.0.1', views.index, name='index'),
]
