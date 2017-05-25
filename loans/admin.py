from django.contrib import admin
from .models import Lend, AssetLend
# Register your models here.

@admin.register(Lend)
class AdminLend(admin.ModelAdmin):
    list_display = ('id', 'reason', 'fkowner', 'fkdepartment', )
    list_filter = ('fkowner', 'fkdepartment', )

@admin.register(AssetLend)
class AdminAssetLend(admin.ModelAdmin):
    list_display = ('id', 'fkasset', 'fklend', )
    list_filter = ('fkasset', 'fklend', )