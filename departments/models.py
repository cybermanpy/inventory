from __future__ import unicode_literals

from django.db import models
from directions.models import Direction
# Create your models here.

class Department(models.Model):
    acronym = models.CharField(max_length=50, blank=False, null=False)
    depname = models.CharField(max_length=140, blank=False, null=False)
    depnumber = models.IntegerField(blank=False, null=False)
    fkdirection = models.ForeignKey(Direction)

    def __str__(self):
        return self.depname

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        ordering = ('id', )