from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Direction(models.Model):
    acronym = models.CharField(max_length=50, blank=False, null=False)
    dirname = models.CharField(max_length=140, blank=False, null=False)
    dirnumber = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.dirname

    class Meta:
        verbose_name = 'Direction'
        verbose_name_plural = 'Directions'
        ordering = ('id', )