from django.shortcuts import render
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response

# Create your views here.
class StudentInfo(APIView):
    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=pk)
            serializer= StudentSerializer(stu)
            return Response (serializer.data)
        stu=Student.objects.all()
        serializer= StudentSerializer(stu , many=True)
        return Response(serializer.data)
    

    def post (self, request):
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Inserted Successfully !!"})
        return Response(serializer.errors)
    

    def put (self,request,pk = None, format = None):
        data = request.data
        stu = Student.objects.get(id=data['id'])
        serializer = StudentSerializer(stu,data = data ,partial = True)
        print(serializer,"hey hahahahahahhaah")
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response(serializer.errors)
    
    def delete(self,request,pk=None):
        stu = Student.objects.get(id=pk)
        stu.delete()
        return Response({"msg":"data deleted successfully"})


