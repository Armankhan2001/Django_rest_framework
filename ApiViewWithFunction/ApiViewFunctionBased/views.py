from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers

# Create your views here.
# @api_view() # by default their is get Method
# def hello_world(request):
#     return Response({"msg":"Hello World"})

# @api_view(['GET','POST'])
# def hello_world(request):
#     if request.method == 'GET':
#         return Response({"msg":"THIS IS GET REQUEST"})
#     if request.method == 'POST':
#         print(request.data)
#         return Response({"msg":"THIS IS POST REQUEST", 'data':request.data})

##########################################     lLETS START WITH THE CRUD     ##################################################################


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializers(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        print(stu,"kakakaka")
        serializer = StudentSerializers(stu,many=True)
        return Response(serializer.data)

    if request.method =='POST':
        serializer = StudentSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response ({"msg":"data Created !!"})
        return Response(serializer.errors)
    
    if request.method =='PUT':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializers(stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response ({"msg":"data Updated Successfully !!"})
        return Response(serializer.errors)
    
    if request.method =='PATCH':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializers(stu, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response ({"msg":"data Updated Successfully !!"})
        return Response(serializer.errors)
    


    if request.method =='DELETE':
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response ({"msg":"data deleted"})
    