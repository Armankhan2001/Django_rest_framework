from django.contrib import admin
from django.urls import path
from .views import StudentInfo

urlpatterns = [
    path('info/',StudentInfo.as_view())
]

