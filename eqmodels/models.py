from __future__ import unicode_literals

from django.db import models
from brands.models import Brand

# Create your models here.

class Eqmodel(models.Model):
    modelname = models.CharField(max_length=140, blank=False, null=False)
    fkbrand = models.ForeignKey(Brand)

    def __str__(self):
        return self.modelname

    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'
        ordering = ('id', )