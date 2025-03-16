from django.shortcuts import render

from rest_framework import generics

from medication.models import Medication
from medication.serializers import MedicationSerializer

# Create your views here.

class MedicationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

class MedicationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    lookup_url_kwarg = 'medication_id'