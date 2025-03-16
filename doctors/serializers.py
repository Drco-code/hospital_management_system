from rest_framework import serializers

from doctors.models import Doctor


from appointments.serializers import AppointmentSerializer


class DoctorSerializer(serializers.ModelSerializer):
    appointment = AppointmentSerializer(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = (
            'doctor_id',
            'user',
            'first_name',
            'last_name',
            'specialization',
            'qualification',
            'contact',
            'email',
            'availability',
            'appointment',
        )

