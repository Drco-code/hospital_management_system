from rest_framework import serializers

from billing.models import Billing
from patients.serializers import PatientSerializer

class BillingsSerializer(serializers.ModelSerializer):

    patient = PatientSerializer( read_only=True)

    class Meta:
        model = Billing
        fields = (
            'billing_id',
            'appointment',
            'total_amount',
            'payment_date',
            'patient',
        )

