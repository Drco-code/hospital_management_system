from django.shortcuts import render

from rest_framework import generics, filters, permissions

from medical_history.serializers import MedicalHistorySerializer
from medical_history.models import MedicalHistory

from medical_history.filters import MedicalHistoryFilter

from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

# Create your views here.


class IsAdminOrOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.patient == request.user



class MedicalHistoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = MedicalHistory.objects.all()
    serializer_class = MedicalHistorySerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    filterset_class = MedicalHistoryFilter
    search_fields = ['diagnosis', 'notes']
    ordering_fields = ['date_of_diagnosis']

    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class MedicalHistoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalHistory.objects.all()
    serializer_class = MedicalHistorySerializer
    lookup_url_kwarg = 'history_id'
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    def get_permissions(self):
        self.permission_classes = [IsAuthenticatedOrReadOnly]
        if self.request.method in ['POST', 'PUT', 'DELETE', 'PATCH']:
            self.permission_classes = [IsAdminOrOwner]
        return super().get_permissions()

