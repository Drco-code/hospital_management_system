from rest_framework import serializers

from billing.models import Billing



class BillingsSerializer(serializers.ModelSerializer):
    patient = serializers.SerializerMethodField() 

    class Meta:
        model = Billing
        fields = (
            'billing_id',
            'appointment',
            'total_amount',
            'payment_date',
            'patient',
        )

    def get_patient(self, instance):
        """
        Custome function to get patient details
        """
        return {
            'patient_id' : instance.patient.patient_id,
            'first_name' : instance.patient.first_name,
            'last_name' : instance.patient.last_name,
            'age' : instance.patient.age,
        }

