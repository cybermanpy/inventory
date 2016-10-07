from __future__ import unicode_literals

from django.db import models
from assets.models import Asset
from departments.models import Department
from owners.models import Owner
from typetransfers.models import TypeTransfer


# Create your models here.

class Transfer(models.Model):
    fkasset = models.ForeignKey(Asset)
    reason = models.CharField(max_length=50, blank=False, null=False)
    fkowner = models.ForeignKey(Owner)
    fkdepartment = models.ForeignKey(Department)
    datetransfer = models.DateField(blank=False, null=False)
    fktypetransfer = models.ForeignKey(TypeTransfer)
    last = models.BooleanField(blank=False, null=False)
    formtransfer = models.FileField(upload_to='media/fileTransfers/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.fkasset.fkdescription.description

    class Meta:
        verbose_name = 'Transfer'
        verbose_name_plural = 'Transfers'
        ordering = ('id', )
    