from rest_framework import serializers

from prescription.models import Prescription
from medication.serializers import MedicationSerializer


class PrescriptionSerializer(serializers.ModelSerializer):

    medication = MedicationSerializer(read_only=True)

    class Meta:
        model = Prescription
        fields = (
            'prescription_id',
            'appointment',
            'medication',
            'instruction',
        )

