from rest_framework import serializers

class StudentSerializers(serializers.Serializer):
    id=serializers.IntegerField() # added id here which is not in model just to show the id to the users
    Name = serializers.CharField( max_length=50)
    Place = serializers.CharField( max_length=50)
    City = serializers.CharField( max_length=50)