from django.shortcuts import render

from rest_framework import generics

from staff.models import Staff
from staff.serializers import StaffSerializer

# Create your views here.

class StaffListCreateAPIView(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class StaffRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    lookup_url_kwarg = 'staff_id'
