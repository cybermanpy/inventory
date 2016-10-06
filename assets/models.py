from __future__ import unicode_literals

from django.db import models
from funders.models import Funder
from descriptions.models import Description
from eqmodels.models import Eqmodel
from providers.models import Provider
from statuses.models import Status
from conservations.models import Conservation


# Create your models here.

class Asset(models.Model):
    fkdescription = models.ForeignKey(Description)
    fkeqmodel = models.ForeignKey(Eqmodel)
    serial = models.CharField(max_length=140, blank=True, null=True)
    fkfunder = models.ForeignKey(Funder)
    codpat = models.CharField(max_length=20, blank=True, null=True)
    features = models.TextField(blank=True, null=True)
    references = models.CharField(max_length=140, blank=True, null=True)
    fkprovider = models.ForeignKey(Provider)
    datebuy = models.DateField(blank=True, null=True)
    price = models.IntegerField(blank=False, null=False)
    warranty = models.CharField(max_length=50, blank=False, null=False)
    obswarranty = models.CharField(max_length=140, blank=False, null=False)
    fkstatus = models.ForeignKey(Status)
    fkconservation = models.ForeignKey(Conservation)
    asstfather = models.IntegerField(blank=True, null=True)
