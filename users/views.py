from django.shortcuts import render

from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer


# Create your views here.

class UserListCreataAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer