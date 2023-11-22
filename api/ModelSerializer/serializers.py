from rest_framework import serializers
from .models import Student


#Validators
def start_with_r(value):
    if value[0].lower()!='a':
        raise serializers.ValidationError('Name Should Start with a ')

# Model Serializer has to wite only 4 line code for crud operations we dont have to write create update functions and serializers fields..
# Form and ModelForm both are like Serializer and ModelSerializer
class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[start_with_r])
    # name = serializers.CharField(read_only=True) # cannot add the name we can only read  or we can write multiple read_only fields as below
    class Meta:
        model = Student
        fields = ['id','name','roll_no','city']
        # read_only_fields=["name","roll_no"]
        # extra_kwargs = {'name':{'read_only':True}}









# VALIDATIONS OF THREETYPES CAN BE USED AS WE USED IN REGULAR SERIALIZERS FIELDLEVEL, OBJECT LEVEL AND VALIDATORS
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