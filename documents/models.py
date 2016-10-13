from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Document(models.Model):
    desdocument = models.CharField(max_length=140, blank=False, null=False)

    def __str__(self):
        return self.desdocument

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
        ordering = ('id', )