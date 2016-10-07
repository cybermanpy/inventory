from django.contrib import admin
from .models import Owner
# Register your models here.

@admin.register(Owner)
class AdminOwner(admin.ModelAdmin):
    list_display = ('fullname', 'identy', 'fkposition', 'fkstatus')
    list_filter = ('fkposition', )