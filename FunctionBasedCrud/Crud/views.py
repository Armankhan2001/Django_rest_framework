from django.shortcuts import render
from .models import Student
from rest_framework.parsers import JSONParser
import io
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from json import JSONDecodeError    # used in try accept block code optional
# Create your views here.


@csrf_exempt 
def StudentInfo(request):
    if request.method == "GET":
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
        
    if request.method == "POST":
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
    
    if request.method == "PUT":
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
    
    if request.method == "DELETE":
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

    


# Same Code Below With Try Axcept Block
# def StudentInfo(request):
#     if request.method == "GET":
#         json_data = request.body
#         if not json_data:
#             stu = Student.objects.all()
#             serializer = StudentSerializer(stu, many=True)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type="application/json")
#         try:
#             stream = io.BytesIO(json_data)
#             pythondata = JSONParser().parse(stream)
#         except JSONDecodeError as e:
#             return JsonResponse({"error": f"Failed to parse JSON data: {str(e)}"}, status=400)

#         id = pythondata.get('id', None)
#         if id is not None:
#             try: # try Except block is used when we know that the code can throughout error we put the code in try block which can through error
#                 stu = Student.objects.get(id=id)
#                 serializer = StudentSerializer(stu)
#                 json_data = JSONRenderer().render(serializer.data)
#                 return HttpResponse(json_data, content_type="application/json")
#             except Student.DoesNotExist:
#                 return JsonResponse({"error": "Student not found."}, status=404)

        











