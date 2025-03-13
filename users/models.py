from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractUser):

    class UserRole(models.TextChoices):
        ADMIN = 'AD', _('Admin')
        PATIENT = 'PA', _('PATIENT')
        DOCTOR = 'DO', _('Doctor')
        NURSE = 'NU', _('Nurse')

    user_role = models.CharField(_("Role"), max_length=2, choices=UserRole.choices)




    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

    # def __str__(self):
    #     return f"{self.username} ({self.get_role_display()})"
