from django.shortcuts import render


from rest_framework import generics

from billing.models import Billing
from billing.serializers import BillingsSerializer

# Create your views here.

class BillingsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingsSerializer

class BillingRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingsSerializer
    lookup_field = 'billing_id'



