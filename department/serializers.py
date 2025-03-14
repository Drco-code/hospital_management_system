from rest_framework import serializers

from department.models import Department


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = (
            'department_id',
            'name',
            'description'
        )