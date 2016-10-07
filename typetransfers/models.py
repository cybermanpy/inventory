from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TypeTransfer(models.Model):
    destypetransfer = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.destypetransfer

    class Meta:
        verbose_name = 'Type Transfer'
        verbose_name = 'Types Tranfers'
        ordering = ('id', )