from rest_framework import serializers

from doctors.models import Doctor


class DoctorSerializer(serializers.ModelSerializer):

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
        )