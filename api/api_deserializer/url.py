from django.contrib import admin
from django.urls import path
from api_deserializer import views


urlpatterns = [
    path('stucreate/', views.StudentCreate)
]

