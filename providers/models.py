from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Provider(models.Model):
    provname = models.CharField(max_length=140, blank=False, null=False)
    contact = models.CharField(max_length=140, blank=False, null=False)
    phone = models.CharField(max_length=50, blank=False, null=False)
    direction = models.CharField(max_length=140, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    web = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.provname

    class Meta:
        verbose_name = 'Provider'
        verbose_name_plural = 'Providers'
        ordering = ('id', )