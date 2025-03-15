from django.db import models

import uuid
from django.utils.translation import gettext_lazy as _

# from prescription.models import Prescription

# Create your models here.

class Medication(models.Model):

    medication_id = models.UUIDField(_("Medication ID"), primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Medication Name"), max_length=100)
    dosage = models.TextField(_("Medication Dosage"))
    frequency = models.TextField(_("Medication Frequency"))
    # presciption = models.ForeignKey(Prescription, verbose_name=_("Prescription"), on_delete=models.CASCADE)
    manufacturer = models.CharField(_("Medication Manufacturer"), max_length=100)
    side_effects = models.TextField(_("Medication Side Effects"))
    created_at = models.DateTimeField(_("Creation Date"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated Date"), auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.dosage}) - {self.manufacturer}"