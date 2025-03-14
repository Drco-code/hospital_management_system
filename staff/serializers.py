from rest_framework import serializers

from staff.models import Staff

class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields =(
            'staff_id',
            'user',
            'first_name',
            'last_name',
            'department',
            'role',
            'contact',
            'email',
        )