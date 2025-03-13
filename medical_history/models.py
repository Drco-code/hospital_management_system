from django.db import models
from patients.models import Patient


import uuid
from django.utils.translation import gettext_lazy as _

# Create your models here.

class MedicalHistory(models.Model):
    history_id = models.UUIDField(_("Medical History ID"), primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient, verbose_name=_("Patient"), on_delete=models.CASCADE)
    diagnosis = models.TextField(_("Daignosis"))
    date_of_diagnosis = models.DateField(_("Diagnosis Date"), null=False)
    notes = models.TextField(_("Additional Notes"))
    created_at = models.DateTimeField(_("Creation Date"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated Date"), auto_now=True)

