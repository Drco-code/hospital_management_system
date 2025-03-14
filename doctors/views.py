from django.shortcuts import render

from rest_framework import generics


from doctors.models import Doctor
from doctors.serializers import DoctorSerializer

# Create your views here.

class DoctorsListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
