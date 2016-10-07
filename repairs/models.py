from __future__ import unicode_literals

from django.db import models
from assets.models import Asset
from providers.models import Provider

# Create your models here.
class Repair(models.Model):
    fkasset = models.ForeignKey(Asset)
    reason = models.CharField(max_length=140, blank=False, null=False)
    solution = models.CharField(max_length=140, blank=True, null=True)
    fkprovider = models.ForeignKey(Provider)
    datebreak = models.DateField(blank=False, null=False)
    datefixed = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.fkasset

    class Meta:
        verbose_name = 'Repair'
        verbose_name_plural = 'Repairs'
        ordering = ('id', )