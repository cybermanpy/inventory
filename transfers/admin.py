from django.contrib import admin
from .models import Transfer
# Register your models here.

@admin.register(Transfer)
class AdminTransfer(admin.ModelAdmin):
    list_display = ('id', 'fkasset', 'reason', 'fkowner', 'fkdepartment', 'datetransfer', 'fktypetransfer', 'last', )
    list_filter = ('fkasset', 'fkdepartment', 'fktypetransfer', )