from django.shortcuts import render

from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer

from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.

class UserListCreataAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "id" # Ensures lookup by 'id' in the URL
    permission_classes = [IsAuthenticated] # Applies Session Auth on the view
    authentication_classes = [JWTAuthentication] # applies JWT ath on the view

    