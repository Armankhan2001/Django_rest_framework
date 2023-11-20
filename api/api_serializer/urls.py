from django.contrib import admin
from django.urls import path
from api_serializer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/<int:pk>', views.Student_details),
    path('stuinfo/', views.Student_list)
]