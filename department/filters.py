import django_filters

from department.models import Department

class DepartmentFilter(django_filters.FilterSet):

    class Meta:
        model = Department
        fields = {
            "name": ['iexact'],
            "description": ['icontains', 'iexact']
        }