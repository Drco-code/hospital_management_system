from django.db import models

from medication.models import Medication
from appointments.models import Appointment

import uuid
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Prescription(models.Model):

    prescription_id = models.UUIDField(_("Prescription ID"), primary_key=True, default=uuid.uuid4, editable=False)
    appointment = models.ForeignKey(Appointment, verbose_name=_("Appointment"), on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, verbose_name=_("Medication"), on_delete=models.CASCADE)
    instruction = models.TextField(_("Instructions"))
    created_at = models.DateTimeField(_("Creation Date"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated Date"), auto_now=True)