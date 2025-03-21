from rest_framework import serializers


from appointments.models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Appointment
        fields = (  
            'appointment_id' ,
            'patient',
            'doctor',
            'appointment_date',
            'appointment_status',
            'reason_visiting',
        )