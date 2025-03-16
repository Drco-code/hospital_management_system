from django.shortcuts import render

from rest_framework import generics, filters, permissions

from medication.models import Medication
from medication.serializers import MedicationSerializer
from medication.filters import MedicalFilter

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated

# Create your views here.

class IsAdminOrOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.medication.user == request.user




class MedicationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    filter_backends = [
        filters.SearchFilter    
    ]

    filterset_class = MedicalFilter
    search_fields = ['name', 'manufacturer', 'side_effects']

    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class MedicationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    lookup_url_kwarg = 'medication_id'
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    def get_permissions(self):

        self.permission_classes = [IsAuthenticatedOrReadOnly]
        if self.request.method == ['POST', 'DELETE', 'PUT', 'PATCH']:
            self.permission_classes = [IsAdminOrOwner]
        return super().get_permissions()