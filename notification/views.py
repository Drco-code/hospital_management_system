from django.shortcuts import render

from rest_framework import generics, filters

from django_filters.rest_framework import DjangoFilterBackend

from notification.models import Notification
from notification.serializers import NotificationSerializer

from notification.filters import NotificationFilter

from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser

# Create your views here.



class NotificationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend
    ]

    filterset_class = NotificationFilter
    search_fields = ['message', 'notification_type']

    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]


class NotificationRetieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    lookup_url_kwarg = "notification_id"

    
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]

