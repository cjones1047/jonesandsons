from django.urls import path
from . import views

app_name = 'jonesandsons_pictures'

urlpatterns = [
    path('gallery/', views.picturesApi, name='gallery')
]