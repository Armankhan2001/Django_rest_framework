"""
URL configuration for GenericapiviewModelmixins project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ModelMixins.views import StudentGP
from ModelMixins.views import StudentRUD
# from ModelMixins.views import StudentRetrieve
# from ModelMixins.views import StudentUpdate
# from ModelMixins.views import StudentDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentsapi/', StudentGP.as_view()),
    path('studentsapi/<int:pk>/',StudentRUD.as_view())
    ]
