from django.shortcuts import render


from rest_framework import generics, permissions

from prescription.models import Prescription
from prescription.serializers import PrescriptionSerializer

from medication.models import Medication
from medication.serializers import MedicationSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly


# Create your views here.

class IsAdminOrOwner(permissions.BasePermission):
    """
    Custom function to get the admin or owner(of the obj)
    """

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.prescriptions == request.user
    


class PrescriptionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Prescription.objects.order_by('prescription_id')
    serializer_class = PrescriptionSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    def get_permissions(self):
        self.permission_classes = [IsAuthenticatedOrReadOnly]
        if self.request.method == ['POST']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class PrescriptionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    lookup_url_kwarg = 'prescription_id'
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    def get_permissions(self):
        self.permission_classes = [IsAuthenticatedOrReadOnly]
        if self.request.method == ['POST', 'DELETE', 'PUT', 'PATCH']:
            self.permission_classes = [IsAdminOrOwner]
        return super().get_permissions()
    

class PrescriptionMedicationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    lookup_url_kwarg = 'medication_id'
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    def get_permissions(self):
        self.permission_classes = [IsAuthenticatedOrReadOnly]
        if self.request.method == ['POST', 'DELETE', 'PUT', 'PATCH']:
            self.permission_classes = [IsAdminOrOwner]
        return super().get_permissions()
    
