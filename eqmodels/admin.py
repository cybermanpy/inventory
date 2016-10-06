from django.contrib import admin
from .models import Eqmodel
# Register your models here.

@admin.register(Eqmodel)
class AdminEqmodel(admin.ModelAdmin):
    list_display = ('id', 'modelname', 'fkbrand')
    list_filter = ('fkbrand', )