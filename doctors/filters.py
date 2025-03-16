import django_filters 

from doctors.models import Doctor


class DoctorFilter(django_filters.FilterSet):

    class Meta:
        model = Doctor
        fields = {
            "first_name": ['icontains'],
            "last_name": ['icontains'],
            "specialization": ['icontains'],
            "qualification": ['exact'],
        }