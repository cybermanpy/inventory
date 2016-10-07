from django.contrib import admin
from .models import Repair
# Register your models here.

@admin.register(Repair)
class AdminTransfer(admin.ModelAdmin):
    list_display = ('id', 'fkasset', 'reason', 'solution', 'fkprovider', 'datebreak', 'datefixed', )
    list_filer = ('fkasset', 'fkprovider', )