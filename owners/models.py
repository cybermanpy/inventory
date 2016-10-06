from __future__ import unicode_literals

from django.db import models
from statuses.models import Status
from positions.models import Position

# Create your models here.

class Owner(models.Model):
    fullname = models.CharField(max_length=140, blank=False, null=False)
    identy = models.IntegerField(blank=False, null=False)
    fkposition = models.ForeignKey(Position)
    fkstatus = models.ForeignKey(Status)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Owner'
        verbose_name_plural = 'Owners'
        ordering = ('id', )