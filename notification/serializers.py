from rest_framework import serializers

from notification.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Notification
        fields = (
            'notification_id',
            'user',
            'message',
            'notification_type',
            'is_read',
        )