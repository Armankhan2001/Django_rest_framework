from rest_framework import serializers
from.models import Student

class StudentSerializers(serializers.Serializer):
    Name = serializers.CharField( max_length=50)
    roll_no = serializers.IntegerField()
    city = serializers.CharField(max_length=20)


    
    #for deserializer below 2 line importand and few lines in views
    def create(self, validate_data):
        return Student.objects.create(**validate_data)