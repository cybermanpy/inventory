from __future__ import unicode_literals

from django.db import models
from assets.models import Asset
from departments.models import Department
from owners.models import Owner


# Create your models here.
class Lend(models.Model):
    reason = models.CharField(max_length=50, blank=False, null=False)
    fkowner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    fkdepartment = models.ForeignKey(Department, on_delete=models.CASCADE)
    datelend = models.DateField(blank=False, null=False)
    lastlend = models.BooleanField(blank=False, null=False)
    devolution = models.DateField(blank=True, null=True)
    details = models.ManyToManyField(Asset, through='AssetLend')
    formlend = models.FileField(upload_to='loans/%Y/%m/%d/', blank=True, null=True)
    
    def __str__(self):
        return self.reason

    class Meta:
        verbose_name = 'Lend'
        verbose_name_plural = 'Loans'
        ordering = ('id', )        

class AssetLend(models.Model):
    fkasset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    fklend = models.ForeignKey(Lend, on_delete=models.CASCADE)

    def __str__(self):
        return self.fkasset.fkdescription.description

    class Meta:
        verbose_name = 'Asset Lend'
        verbose_name_plural = 'Asset Loans'
        ordering = ('id', )