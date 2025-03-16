from django.shortcuts import render

from rest_framework import generics


from doctors.models import Doctor
from doctors.serializers import DoctorSerializer

from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer

# Create your views here.

class DoctorsListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorReteiveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    lookup_url_kwarg = 'doctor_id'

class DoctorAppointmentReteiveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    lookup_url_kwarg = 'appointment_id'