from django.db import models
from patients.models import Patient
from doctors.models import Doctor

import uuid
from django.utils.translation import gettext_lazy as _

# Create your models here.

class AppointmentStatus(models.TextChoices):
    PENDING = 'PN', _('PENDING')
    COMPLETED = 'CP', _('COMPLETED')
    CANCELLED = 'CL', _('CANCELLED')

class Appointment(models.Model):
    appointment_id = models.UUIDField(_("Appointment ID"), primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient, verbose_name=_("Patient"), on_delete=models.CASCADE, related_name='appointment')
    doctor = models.ForeignKey(Doctor, verbose_name=_("Doctor"), on_delete=models.CASCADE, related_name='appointment')
    appointment_date = models.DateTimeField(_("Appointment Date"))
    appointment_status = models.CharField(_("Appointment Status"), max_length=2, choices=AppointmentStatus.choices, default=AppointmentStatus.PENDING)
    reason_visiting = models.TextField(_("Reason For Visit"))
    created_at = models.DateTimeField(_("Creation Date"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated Date"), auto_now=True)
    
    def __str__(self):
        return f"Appointment {self.appointment_id} - {self.patient.first_name} with Dr. {self.doctor.last_name} on {self.appointment_date.strftime('%Y-%m-%d %H:%M')}"
