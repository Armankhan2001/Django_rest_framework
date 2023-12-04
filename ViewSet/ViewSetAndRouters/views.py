from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

# Create your views here.

class StudentInfo(viewsets.ViewSet):
    def list(self,request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response (serializer.data)
    
    def retrieve(self,request,pk):
        if id is not None:
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        
    def create(self, request):
        Serializer = StudentSerializer(data = request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response({"msg":"data created  Successfully"})
        
    def update(self,request,pk):
        data = request.data
        print(data["id"])
        stu = Student.objects.get(id = pk)
        serializer = StudentSerializer(stu,data = data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def destroy(self,request,pk):
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response ({"msg":"Data Deleted Successfully !!"})
        
    

