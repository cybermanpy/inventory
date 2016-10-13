from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Feature(models.Model):
    desfeature = models.CharField(max_length=140, blank=False, null=False)

    def __str__(self):
        return self.desfeature

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'