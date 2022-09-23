from django.urls import path
from . import views

app_name = 'jonesandsons_pictures'

urlpatterns = [
    path('', views.index, name='index')
]