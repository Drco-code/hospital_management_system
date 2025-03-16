from django.db import models
from patients.models import Patient
from appointments.models import Appointment

import uuid
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Billing(models.Model):
    billing_id = models.UUIDField(_("Billing ID"), primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient, verbose_name=_("Patient"), on_delete=models.CASCADE, related_name='patient')
    appointment = models.ForeignKey(Appointment, verbose_name=_("Appointment"), on_delete=models.CASCADE)
    total_amount = models.DecimalField(_("Total amount"), max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(_("Payment Date"), null=False)
    created_at = models.DateTimeField(_("Creation Date"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated Date"), auto_now=True)

    def __str__(self):
        return f"Billing for {self.patient} - Appointment {self.appointment.id} - Amount {self.total_amount}"

