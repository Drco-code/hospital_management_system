from django.shortcuts import render

from rest_framework import generics

from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer

# Create your views here.

class AppointmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer