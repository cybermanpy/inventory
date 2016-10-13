from __future__ import unicode_literals

from django.db import models
from funders.models import Funder
from descriptions.models import Description
from eqmodels.models import Eqmodel
from providers.models import Provider
from statuses.models import Status
from conservations.models import Conservation
from features.models import Feature
from documents.models import Document


# Create your models here.

class Asset(models.Model):
    fkdescription = models.ForeignKey(Description)
    fkeqmodel = models.ForeignKey(Eqmodel)
    serial = models.CharField(max_length=140, blank=True)
    fkfunder = models.ForeignKey(Funder)
    codpat = models.CharField(max_length=20, blank=True)
    features = models.ManyToManyField(Feature, through='DetailFeature')
    observation = models.CharField(max_length=140, blank=True, null=True)
    fkprovider = models.ForeignKey(Provider)
    datebuy = models.DateField(blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    fkdocument = models.ForeignKey(Document)
    docnumber = models.IntegerField(blank=False, null=False)
    warranty = models.CharField(max_length=50, blank=False, null=False)
    obswarranty = models.CharField(max_length=140, blank=True)
    fkstatus = models.ForeignKey(Status)
    fkconservation = models.ForeignKey(Conservation)
    assetfather = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return "%s %s %s" %(self.id, self.fkdescription.description, self.fkeqmodel)

    class Meta:
        verbose_name = 'Asset'
        verbose_name_plural = 'Assets'
        ordering = ('id', )

class DetailFeature(models.Model):
    fkasset = models.ForeignKey(Asset)
    fkfeature = models.ForeignKey(Feature)
    details = models.TextField(blank=False, null=False)

    def __str__(self):
        return "%s %s" %(self.fkasset, self.fkfeature)

    class Meta:
        verbose_name = 'Detail Feature'
        verbose_name_plural = 'Details Features'
        ordering = ('fkasset', )