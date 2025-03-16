
from patients.serializers import PatientSerializer

from patients.models import Patient

from medical_history.models import MedicalHistory
from medical_history.serializers import MedicalHistorySerializer

from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer

from django_filters.rest_framework import DjangoFilterBackend

from patients.filters import PatientFilter
from rest_framework import filters

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import generics, permissions

# Create your views here.


class PatientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [
        # DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # filterset_fields = ['user', 'patient_id','first_name', 'last_name', 'contact']
    
    filterset_class = PatientFilter

    # Enable searching and ordering
    search_fields = ['first_name', 'last_name', 'contact', 'age', 'gender']
    ordering_fields = ['age', 'gender']

    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

        
    def get_permissions(self):
        """
        Custom function to get only the admin to SEND a POST request
        """

        self.permission_classes = [IsAuthenticatedOrReadOnly]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission: Only allow the owner or an admin to update/delete a patient record.
    """
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff  # Only admins can update/delete patients.

class PatientRetriveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_url_kwarg = 'patient_id'
    authentication_classes = [JWTAuthentication, SessionAuthentication]


    def get_permissions(self):
        """
        Custom function for only admin and owner to make POST 'POST', 'DELETE', 'PUT', 'PATCH' request
        """
        self.permission_classes = [IsAuthenticatedOrReadOnly]
        if self.request.method == ['POST', 'DELETE', 'PUT', 'PATCH']:
            self.permission_classes = [IsOwnerOrAdmin]
        return super().get_permissions()


class PatientMedicalRecordsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalHistory.objects.all()
    serializer_class = MedicalHistorySerializer
    lookup_url_kwarg = 'history_id'

    def get_permissions(self):
        """
        Custom function for only admin and owner to make POST 'POST', 'DELETE', 'PUT', 'PATCH' request
        """
        self.permission_classes = [IsAuthenticatedOrReadOnly]
        if self.request.method == ['POST', 'DELETE', 'PUT', 'PATCH']:
            self.permission_classes = [IsOwnerOrAdmin]
        return super().get_permissions()
    
class PatientAppointmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    lookup_url_kwarg = 'appointment_id'

    def get_permissions(self):
        """
        Custom function for only admin and owner to make POST 'POST', 'DELETE', 'PUT', 'PATCH' request
        """
        self.permission_classes = [IsAuthenticatedOrReadOnly]
        if self.request.method == ['POST', 'DELETE', 'PUT', 'PATCH']:
            self.permission_classes = [IsOwnerOrAdmin]
        return super().get_permissions()
    
