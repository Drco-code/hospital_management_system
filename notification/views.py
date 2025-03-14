from django.shortcuts import render

from rest_framework import generics

from notification.models import Notification
from notification.serializers import NotificationSerializer

# Create your views here.



class NotificationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
