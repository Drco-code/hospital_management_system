from django.shortcuts import render

from rest_framework import generics

from notification.models import Notification
from notification.serializers import NotificationSerializer

# Create your views here.



class NotificationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class NotificationRetieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    lookup_url_kwarg = "notification_id"

