from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from . models import Student
from rest_framework.response import Response
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# Create your views here.



# @method_decorator(csrf_exempt,name='dispatch')
@api_view(['GET','POST'])
def StudentInfo(request):
    if request.method == "GET":
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        for i in serializer.data:
            id=i['id']
            full_name=i['f_name'] +" "+ i['l_name']
            fullname={"full_name":full_name}
            print(fullname)
            stu= Student.objects.get(id=id)
            if stu :
                serializer=StudentSerializer(stu, data = fullname, partial = True)
                if serializer.is_valid():
                    serializer.save()
            else:
                return Response({"msg":"data not found"})
        
        return Response({"msg":"Full_name updated successfully"})
    
        


    # if request.method == "GET":
    #     ide = request.data
    #     if ide:
    #         stu = Student.objects.get(id=ide['id'])
    #         serializer = StudentSerializer(stu)
    #         return Response(serializer.data)
    #     stu = Student.objects.all()
    #     serializer = StudentSerializer(stu, many = True)
    #     return Response(serializer.data)

    if request.method == "POST":
        serializer = StudentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"data created successfully !!"})
        return Response(serializer.errors)
