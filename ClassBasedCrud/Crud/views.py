from django.shortcuts import render
from .models import Student
from rest_framework.parsers import JSONParser
import io
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
@method_decorator(csrf_exempt, name='dispatch')
class StudentInfo(View):
    def get (self,request, *args, **kwargs):
        json_data = request.body
        if not json_data:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type="application/json")
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type="application/json")
    

    def post (self,request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)#stream liye json data ko python data me badalne k liye
        pythondata = JSONParser().parse(stream) # parser k through streamed data ko python data me convert kiya
        serializer = StudentSerializer(data=pythondata) # serializer k through python data ko complex data me convert kiya
        if serializer.is_valid():
            serializer.save()                               #successfully saved hogaya complex data me python data through serializer.
            res = {"msg":"Data Posted Successfully !!"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = "application/json")
    

    def put (self,request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)#stream liye json data ko python data me badalne k liye
        pythondata = JSONParser().parse(stream) # parser k through streamed data ko python data me convert kiya
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=pythondata, partial=True) # partial update dosent need all fields in postman # serializer k through python data ko complex data me convert kiya
        if serializer.is_valid():
            serializer.save()                               #successfully saved hogaya complex data me python data through serializer.
            res = {"msg":"Data Updated Successfully !!"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = "application/json")
    

    def delete (self,request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {"msg":"data deleted Successfully !! "}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type = "application/json")
        return JsonResponse(res, safe = False) # insted of above two line we can directly use jsonresponse # safe false is used if data not in dict.











