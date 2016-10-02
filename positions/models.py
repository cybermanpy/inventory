from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Position(models.Model):
    description = models.CharField(max_length=140, blank=False, null=False)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'
        ordering = ('id',)