import django_filters

from medical_history.models import MedicalHistory


class MedicalHistoryFilter(django_filters.FilterSet):

    class Meta:
        model = MedicalHistory
        fields = {
            "diagnosis": ['icontains', 'iexact'],
            "notes": ['icontains', 'iexact'],
            "date_of_diagnosis": ['lte', 'gte', 'exact'],
        }