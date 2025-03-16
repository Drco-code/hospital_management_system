from django.shortcuts import render

from rest_framework import generics

from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer

from datetime import datetime

# Create your views here.

class AppointmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    lookup_url_kwarg = 'appointment_id'


class UpcomingAppointmentListAPIAPIView(generics.ListAPIView):
    serializer_class = AppointmentSerializer


    def get_queryset(self):
        """
        Return all upcoming appointments (appointments with a future date).
        """
        current_datetime = datetime.now()
        return Appointment.objects.filter(appointment_date__gte=current_datetime).order_by('appointment_date')
    
class PastAppointmentListAPIAPIView(generics.ListAPIView):
    serializer_class = AppointmentSerializer


    def get_queryset(self):
        """
        Return all upcoming appointments (appointments with a future date).
        """
        current_datetime = datetime.now()
        return Appointment.objects.filter(appointment_date__lt=current_datetime).order_by('appointment_date')
    
    

    