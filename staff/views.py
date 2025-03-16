from django.shortcuts import render

from rest_framework import generics,filters

from staff.models import Staff
from staff.serializers import StaffSerializer

from staff.filters import StaffFilter

from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class StaffListCreateAPIView(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    filter_backends = [
        filters.SearchFilter
    ]

    filterset_class = StaffFilter
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'first_name', 'last_name', 'role', 'contact']

    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]



class StaffRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    lookup_url_kwarg = 'staff_id'

    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]

