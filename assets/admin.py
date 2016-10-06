from django.contrib import admin
from .models import Asset
# Register your models here.

@admin.register(Asset)
class AdminAsset(admin.ModelAdmin):
    list_display = ('id', 'fkdescription', 'fkeqmodel', 'serial')
    list_filter = ('fkeqmodel', )