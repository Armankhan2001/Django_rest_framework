from django.contrib import admin
from django.urls import path
from .views import StudentInfo

urlpatterns = [
    path('info/',StudentInfo)
    # path('info/',StudentInfo.as_view())  #  this url for class based view
]

