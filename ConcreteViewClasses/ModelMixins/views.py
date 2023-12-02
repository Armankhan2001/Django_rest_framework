# from django.shortcuts import render
from.models import Student
from .serializers import StudentSerializers
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
# from rest_framework.generics import RetrieveDestroyAPIView


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers



#COMBINE THE APIVIEWS
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

class StudentGP(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class StudentRUD(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers