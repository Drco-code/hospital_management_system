from django.db import models
from users.models import User

import uuid
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Notification(models.Model):

    class NotificationType(models.TextChoices):
        APPOINTMENT = 'AP', _('Appointment Remainder')
        PAYMENT = 'PA', _('Payment ALERT')
        SYSTEM = 'SY', _('System Message')
        OTHER = 'OT', _('Other')

    notification_id = models.UUIDField(_("Notification ID"), primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    message = models.TextField(_("Message"))
    notification_type = models.CharField(_("Notification Type"), max_length=2, choices=NotificationType.choices, default=NotificationType.OTHER)
    is_read = models.BooleanField(_("Is Read"), default=False)
    created_at = models.DateTimeField(_("Creation Date"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated Date"), auto_now=True)
    
    def __str__(self):
        return f"{self.user} - {self.notification_type} - {'Read' if self.is_read else 'Unread'}"