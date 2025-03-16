from django.shortcuts import render

from rest_framework import generics, filters, permissions

from appointments.filters import AppointmentFilter

from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated

from datetime import datetime

# Create your views here.


class ISAdminOrOwner(permissions.BasePermission):
    """
    Custom field to get the Admin or Owner(of an obj)
    """

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.appointment == request.user




class AppointmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    # Set up filtering
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    filterset_class = AppointmentFilter
    search_fields = ['appointment_status']
    ordering_fields = ['appointment_date']

    authentication_classes = [JWTAuthentication, SessionAuthentication]

    def get_permissions(self):
        self.permission_classes = [IsAuthenticatedOrReadOnly]
        if self.request.method == ['POST']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()



class AppointmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    lookup_url_kwarg = 'appointment_id'
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    def get_permissions(self):
        self.permission_classes = [IsAuthenticatedOrReadOnly]
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


class UpcomingAppointmentListAPIAPIView(generics.ListAPIView):
    serializer_class = AppointmentSerializer

    # setup authentication
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        """
        Return all upcoming appointments (appointments with a future date).
        """
        current_datetime = datetime.now()
        return Appointment.objects.filter(appointment_date__gte=current_datetime).order_by('appointment_date')
    
class PastAppointmentListAPIAPIView(generics.ListAPIView):
    serializer_class = AppointmentSerializer

    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        """
        Return all upcoming appointments (appointments with a future date).
        """
        current_datetime = datetime.now()
        return Appointment.objects.filter(appointment_date__lt=current_datetime).order_by('appointment_date')
    
    

    