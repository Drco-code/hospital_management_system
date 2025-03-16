import django_filters

from patients.models import Patient

class PatientFilter(django_filters.FilterSet):

    class Meta:
        model = Patient
        fields = {
            'first_name': ['icontains'],
            'last_name': ['icontains'],
            'gender': ['exact', 'lte', 'gte'],
            'contact': ['icontains'],
            'age': ['exact', 'lte', 'gte'],
        }

