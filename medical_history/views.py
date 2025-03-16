from django.shortcuts import render

from rest_framework import generics

from medical_history.serializers import MedicalHistorySerializer
from medical_history.models import MedicalHistory
# Create your views here.

class MedicalHistoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = MedicalHistory.objects.all()
    serializer_class = MedicalHistorySerializer

class MedicalHistoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalHistory.objects.all()
    serializer_class = MedicalHistorySerializer
    lookup_url_kwarg = 'history_id'

