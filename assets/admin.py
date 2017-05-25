from django.contrib import admin
from .models import Asset, DetailFeature
# Register your models here.

@admin.register(Asset)
class AdminAsset(admin.ModelAdmin):
    list_display = ('id', 'assetfather', 'fkdescription', 'fkeqmodel', 'serial', )
    list_filter = ('fkeqmodel', )

@admin.register(DetailFeature)
class AdminDetailFeature(admin.ModelAdmin):
    list_display = ('id', 'fkasset', 'fkfeature', 'details', )
    list_filter = ('fkasset', 'fkfeature', )