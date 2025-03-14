from rest_framework import serializers
from patients.models import Patient

from medical_history.serializers import MedicalHistorySerializer



class PatientSerializer(serializers.ModelSerializer):
    medical_history = MedicalHistorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Patient
        fields = (
            'patient_id',
            'user',
            'first_name',
            'last_name',
            'age',
            'gender',
            'dob',
            'address',
            'contact',
            'email',
            'emergency_contact',
            'insurance_number',
            'blood_group',
            'medical_history',
        )
        