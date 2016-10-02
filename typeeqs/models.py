from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TypeEq(models.Model):
    name = models.CharField(max_length=140, blank=False, null=False)
    code = models.CharField(max_length=140, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'
        ordering = ('id', )