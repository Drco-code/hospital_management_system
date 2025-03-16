from django.shortcuts import render

from rest_framework import generics, filters, permissions


from doctors.models import Doctor
from doctors.serializers import DoctorSerializer

from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer

from doctors.filters import DoctorFilter

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser


# Create your views here.

class IsAdminOrOwner(permissions.BasePermission):
    """
    Custom function for only admin and owner to make POST 'POST', 'DELETE', 'PUT', 'PATCH' request
    """
    
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.patient == request.user

class DoctorsListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [
        filters.SearchFilter
    ]
    filterset_class = DoctorFilter
    search_fields = [
        'first_name',
        'last_name',
        'specialization',
        'qualification'
    ]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    def get_permissions(self):
        self.permission_classes = [IsAuthenticatedOrReadOnly]
        if self.request.method == ['POST', 'DELETE', 'PUT', 'PATCH']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class DoctorReteiveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    lookup_url_kwarg = 'doctor_id'
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    def get_permissions(self):
        self.permission_classes = [IsAuthenticatedOrReadOnly]
        if self.request.method == ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminOrOwner]
        return super().get_permissions()


class DoctorAppointmentReteiveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    lookup_url_kwarg = 'appointment_id'

    def get_permissions(self):
        self.permission_classes = [IsAuthenticatedOrReadOnly]
        if self.request.method == ['POST', 'DELETE', 'PUT', 'PATCH']:
            self.permission_classes = [IsAdminOrOwner]
        return super().get_permissions()

