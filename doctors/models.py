from django.db import models
from users.models import User

import uuid
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Doctor(models.Model):

    doctor_id = models.UUIDField(_("Doctor ID"), primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    first_name = models.CharField(_("First Name"), max_length=100, blank=False, null=False)
    last_name = models.CharField(_("Last Name"), max_length=100, blank=False, null=False)
    specialization = models.CharField(_("Doctor's Specialization"), max_length=100)
    qualification  = models.CharField(_("Doctor's Qualification"), max_length=100)
    contact = models.CharField(_("Doctor's Contact"), max_length=50)
    email = models.EmailField(_("Doctor's Email"), max_length=254)
    availability = models.JSONField(_("Availability"))
    created_at = models.DateTimeField(_("Creation Date"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated Date"), auto_now=True)
    

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} - {self.specialization}"