from rest_framework import serializers


from medical_history.models import MedicalHistory




class MedicalHistorySerializer(serializers.ModelSerializer):
    patient = serializers.SerializerMethodField()
    
    class Meta:
        model = MedicalHistory
        fields = (
            'history_id',
            'patient',
            'diagnosis',
            'date_of_diagnosis',
            'notes',
        )


    def get_patient(self, obj):
        from patients.serializers import PatientSerializer  # Lazy import here 🚀
        return PatientSerializer(obj.patient).data


