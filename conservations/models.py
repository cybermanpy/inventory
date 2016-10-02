from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Conservation(models.Model):
    description = models.CharField(max_length=140, blank=False, null=False)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Conservation'
        verbose_name_plural = 'Conservations'
        ordering = ('id', )