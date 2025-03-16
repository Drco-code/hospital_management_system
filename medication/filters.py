import django_filters

from medication.models import Medication

class MedicalFilter(django_filters.FilterSet):

    class Meta:
        model = Medication
        fields = {
            "name": ['exact', 'icontains'],
            "manufacturer": ['exact', 'icontains'],
            "side_effects": ['exact', 'icontains'],
        }
