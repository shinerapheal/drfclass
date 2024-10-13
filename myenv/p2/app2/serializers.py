from rest_framework import serializers
from . models import *
from django.contrib.auth.models import User

class EmpSeralizer(serializers.ModelSerializer):

    class Meta:

        model=Emp
        fields='__all__'

    def validate(self, data):
        
        if data['age'] < 18:
            raise serializers.ValidationError('age gr 18')
        elif '@' not in data['email']:
            raise serializers.ValidationError("inapropriaate email")
        return data
    
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:

        model=User
        fields=['id','username','password','email']





