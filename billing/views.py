from django.shortcuts import render


from rest_framework import generics

from billing.models import Billing
from billing.serializers import BillingsSerializer

from patients.models import Patient

# Create your views here.

class BillingsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingsSerializer

class BillingsRetieveUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingsSerializer
    lookup_url_kwarg = 'billing_id'


class PatientBillingListAPIView(generics.ListAPIView):
    serializer_class = BillingsSerializer

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return Billing.objects.filter(patient_id=patient_id)
    



