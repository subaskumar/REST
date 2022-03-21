from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Student

# Here also we can raise  Model validation Errors.

# def rollNO_limit(value):
#     if value > 200:
#         raise ValidationError("seat is full %(value)s')", params={'value': value})

class StudentSerializer(serializers.ModelSerializer):
    # name =  serializers.CharField(max_length = 150)
    # roll = serializers.IntegerField()
    # city = serializers.CharField(max_length = 150)
    class Meta:
        model = Student
        fields = '__all__'
    
    # def validate(self,data):
    #     name = data.get('name')
    #     city = data.get('city')
    #     if name.lower() == 'subas' and city.lower() != 'bbsr':
    #         raise serializers.ValidationError("City must be BBSR")   
    #     return data