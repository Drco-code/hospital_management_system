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


class UpcomingAppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        """
        This method returns all upcoming appoints (from current date and time or in the future) amd order by appointment date"
        """
        current_date_time = datetime.now()

        return Appointment.objects.filter(appointment_date__gte=current_date_time)
    
class PastAppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        """
        This method returns all past appoints (from current date and time or in the future) amd order by appointment date"
        """
        current_date_time = datetime.now()

        return Appointment.objects.filter(appointment_date__lte=current_date_time)
    
