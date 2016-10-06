from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Brand(models.Model):
    brandname = models.CharField(max_length=140, blank=False, null=False)

    def __str__(self):
        return self.brandname

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ('id', )