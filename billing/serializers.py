from rest_framework import serializers

from billing.models import Billing

class BillingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Billing
        fields = (
            'billing_id',
            'patient',
            'appointment',
            'total_amount',
            'payment_date'
        )

