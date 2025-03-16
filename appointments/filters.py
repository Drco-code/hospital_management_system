import django_filters

from appointments.models import Appointment

class AppointmentFilter(django_filters.FilterSet):

    class Meta:
        model = Appointment
        fields = {
            "appointment_date": ['lte', 'gte'],
            "appointment_status": ['exact', 'icontains']
        }
        