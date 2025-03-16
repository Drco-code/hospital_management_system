from django.shortcuts import render


from rest_framework import generics

from prescription.models import Prescription
from prescription.serializers import PrescriptionSerializer

from medication.models import Medication
from medication.serializers import MedicationSerializer


# Create your views here.

class PrescriptionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

class PrescriptionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    lookup_url_kwarg = 'prescription_id'

class PrescriptionMedicationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    lookup_url_kwarg = 'medication_id'


