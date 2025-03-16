from django.shortcuts import render

from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer

from rest_framework.permissions import IsAuthenticated


# Create your views here.

class UserListCreataAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "id"
    permission_classes = [IsAuthenticated]

    