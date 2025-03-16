import django_filters

from staff.models import Staff


class StaffFilter(django_filters.FilterSet):
    user__username = django_filters.CharFilter(lookup_expr="icontains")  # Correct way for ForeignKey field

    class Meta:
        models = Staff
        fields = {
            "first_name": ["iexact","icontains"],
            "last_name": ["iexact","icontains"],
            "role": ["iexact","icontains"],
            "contact": ["iexact","icontains"],
        }