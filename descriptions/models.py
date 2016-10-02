from __future__ import unicode_literals

from django.db import models
from typeeqs.models import TypeEq

# Create your models here.

class Description(models.Model):
    description = models.CharField(max_length=140, blank=False, null=False)
    fktype = models.ForeignKey(TypeEq)