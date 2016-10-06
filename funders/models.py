from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Funder(models.Model):
    fundername = models.CharField(max_length=140, blank=False, null=False)

    def __str__(self):
        return self.fundername

    class Meta:
        verbose_name = 'Funder'
        verbose_name_plural = 'Funders'
        ordering = ('id', )