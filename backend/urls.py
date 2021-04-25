from django.urls import path, include
from . import views

urlpatterns = [
    path('historical/dax', views.historicalDax, name='historical-dax'),
    path('historical/dax/recognition', views.historicalDaxRecognition, name='historical-dax-recognition'),
]