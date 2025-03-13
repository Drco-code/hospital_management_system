from django.db import models
from users.models import User
from department.models import Department

import uuid
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Staff(models.Model):

    class RoleChoices(models.TextChoices):
        ADMIN = 'AD', _('Admin')
        DOCTOR = 'DO', _('Doctor')
        NURSE = 'NU', _('Nurse')
        RECEPTIONIST = 'RE', _('Receptionist')

    staff_id = models.UUIDField(_("Staff ID"), primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE, null=True, blank=True)  # Staff can have a user for login
    first_name = models.CharField(_("First Name"), max_length=100)
    last_name = models.CharField(_("Last Name"), max_length=100)
    department = models.ForeignKey(Department, verbose_name=_("Department"), on_delete=models.SET_NULL, null=True)  # Staff belong to a department
    role = models.CharField(_("Role"), max_length=2, choices=RoleChoices.choices, default=RoleChoices.ADMIN)  # Staff role
    contact = models.CharField(_("Contact"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    created_at = models.DateTimeField(_("Creation Date"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated Date"), auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role} ({self.department.name if self.department else 'No Department'})"