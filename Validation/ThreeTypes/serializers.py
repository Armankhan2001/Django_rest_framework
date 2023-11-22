from rest_framework import serializers
from .models import Student



    
    # VALIDATORS

def start_with_r(value):
    if value[0].lower()!='a':
        raise serializers.ValidationError('Name Should Start with a ')
    
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField( max_length=50, validators = [start_with_r])
    roll_no = serializers.IntegerField()
    city = serializers.CharField( max_length=50)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance,validated_data):
        instance.name =validated_data.get('name',instance.name)
        instance.roll_no =validated_data.get('roll_no',instance.roll_no)
        instance.city =validated_data.get('city',instance.city)
        instance.save()
        return instance
    


    #FIELD LEVEL VALIDATION
    
    def validate_roll_no(self,value):
        if value>=200:
            raise serializers.ValidationError("Seat Full")
        return value
    
    # OBJECT LEVEL VALIDATION

    def validate(self,data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower()== 'asim' and ct.lower()!='mumbai':
            raise serializers.ValidationError('City must be Mumbai')
        return data

