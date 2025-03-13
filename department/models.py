from django.db import models


import uuid
from django.utils.translation import gettext_lazy as _

# Create your models here.
# Department Model
class Department(models.Model):

    department_id = models.UUIDField(_("Department ID"), primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Department Name"), max_length=100, unique=True)
    description = models.TextField(_("Department Description"), blank=True, null=True)
    created_at = models.DateTimeField(_("Creation Date"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated Date"), auto_now=True)

    def __str__(self):
        return self.name