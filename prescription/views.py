from django.shortcuts import render


from rest_framework import generics

from prescription.models import Prescription
from prescription.serializers import PrescriptionSerializer


# Create your views here.

class PrescriptionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer