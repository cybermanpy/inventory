from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Status(models.Model):
    statusname = models.CharField(max_length=140, blank=False, null=False)

    def __str__(self):
        return self.statusname

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'
        ordering = ('id', )