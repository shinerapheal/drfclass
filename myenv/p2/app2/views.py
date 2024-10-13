from django.shortcuts import render,redirect
from rest_framework import viewsets
from . serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


@api_view(['POST'])
def login(request):
    data=request.data
    user=get_object_or_404(User,username=data['username'])
    if not user.check_password(data['password']):
        return Response({"details":"not found"},status=status.HTTP_400_BAD_REQUEST)
    token, create =Token.objects.get_or_create(user=user)
    serializer=UserSerializer(instance=user)
    

        
    return Response({"token":token.key,"user":serializer.data})
    # return redirect('/app2/empdet') // after login view emp details

@api_view(['POST'])
def signup(request):
    data=request.data
    serializer=UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        user=User.objects.get(username=data['username'])
        user.set_password(request.data['password'])
        user.save()
        token=Token.objects.create(user=user)
        return Response({"token":token.key,"user":serializer.data})
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def test(request):
    return

class Empdet(viewsets.ModelViewSet):
    serializer_class=EmpSeralizer
    queryset=Emp.objects.all()




  