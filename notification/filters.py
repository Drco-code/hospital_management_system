import django_filters

from notification.models import Notification

class NotificationFilter(django_filters.FilterSet):

    class Meta:
        model = Notification
        fields = {
            "message": ['icontains', 'iexact'],
            "notification_type": ['exact']
        }