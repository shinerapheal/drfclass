from django.shortcuts import render
from rest_framework import viewsets
from . serializers import *

# Create your views here.
class EmpViewSet(viewsets.ModelViewSet):
    serializer_class=EmpSeralizer
    queryset=Emp.objects.all()
