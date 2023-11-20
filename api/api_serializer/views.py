from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create your views here.
#Queryset :- which has only one column
def Student_details(request, pk):
    stu = Student.objects.get(id= pk)
    print(stu," getting the complex data")
    serializer = StudentSerializers(stu)
    
    '''print(serializer,"serialised complex data into python native dict")
    json_data = JSONRenderer().render(serializer.data)
    print(json_data, " Rendered python native dict into json_data")
    return HttpResponse(json_data, content_type = 'application/json')''' 
    # "we can direclty input jsonresponse just by converting complex data into python native"

    return JsonResponse(serializer.data)



# Create your views here.
#Model Instance :- all the Data
def Student_list(request):
    stu = Student.objects.all()
    print(stu," getting the complex data")
    serializer = StudentSerializers(stu,many=True)

    '''print(serializer,"serialised complex data into python native dict")
    json_data = JSONRenderer().render(serializer.data)
    print(json_data, " Rendered python native dict into json_data")
    return HttpResponse(json_data, content_type = 'application/json')'''

    return JsonResponse(serializer.data, safe = False)   # we had written safe = False bcoz it is a list of data not a dict 