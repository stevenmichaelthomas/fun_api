from django.urls import path
from . import views

urlpatterns = [
    path('', views.getImages, name='images'),
]
