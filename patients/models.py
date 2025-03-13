from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User

import uuid

# Create your models here.

class Patient(models.Model):

    class GenderChoices(models.TextChoices):
        MALE = 'M', _('MALE')
        FEMALE = 'F', _('FEMALE')

    class BloodGroup(models.TextChoices):
        A_POS = 'A+', _('A+')
        A_NEG = 'A-', _('A-')
        B_POS = 'B+', _('B+')
        B_NEG = 'B-', _('B-')
        AB_POS = 'AB+', _('AB+')
        AB_NEG = 'AB-', _('AB-')
        O_POS = 'O+', _('O+')
        O_NEG = 'O-', _('O-')

    patient_id = models.UUIDField(_("Patient ID"), primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    first_name = models.CharField(_("First Name"), max_length=100, blank=False, null=False)
    last_name = models.CharField(_("Last Name"), max_length=100, blank=False, null=False)
    age = models.PositiveIntegerField(_("Patient Age"), null=True, blank=True)
    gender = models.CharField(_("Patient Gender"), choices=GenderChoices.choices, max_length=1, default=GenderChoices.MALE)
    dob = models.DateTimeField(_("Patient Date of Birth"))
    address = models.TextField(_("Patient Address"))
    contact = models.TextField(_("Patient Contact"))
    email = models.EmailField(_("Patient Email"), max_length=254)
    emergency_contact = models.TextField(_("Emergency Contact"))
    insurance_number = models.CharField(_("Insurance Number"), max_length=50)
    blood_group = models.CharField(_("Blood Group"), max_length=3, choices=BloodGroup.choices, default=BloodGroup.O_POS)
    medical_history = models.TextField(_("Medical History"))
    created_at = models.DateTimeField(_("Creation Date"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated Date"), auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.blood_group}"
