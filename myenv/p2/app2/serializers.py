from rest_framework import serializers
from . models import *

class EmpSeralizer(serializers.ModelSerializer):

    class Meta:

        model=Emp
        fields='__all__'




