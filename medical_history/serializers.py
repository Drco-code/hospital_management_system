from rest_framework import serializers



from medical_history.models import MedicalHistory



class MedicalHistorySerializer(serializers.ModelSerializer):
    # patient = serializers.PrimaryKeyRelatedField(read_only=True)  # Only return patient ID

    # patient = serializers.StringRelatedField()  # Returns the __str__() method of Patient

    patient_details = serializers.SerializerMethodField()  # Custom field for patient details


    class Meta:
        model = MedicalHistory
        fields = (
            'history_id',
            'diagnosis',
            'date_of_diagnosis',
            'notes',
            'patient_details',
        )

    def get_patient_details(self, obj):
        """
        Custom Field for returning patient details
        """
        return {
            "patient_id": obj.patient.patient_id,
            "first_name": obj.patient.first_name,
            "last_name": obj.patient.last_name,
            "age": obj.patient.age,
            "gender": obj.patient.gender,
            "email": obj.patient.email,
        }
    
    
