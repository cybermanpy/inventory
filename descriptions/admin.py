from django.contrib import admin
from .models import Description

# Register your models here.
@admin.register(Description)
class AdminDescription(admin.ModelAdmin):
    list_display = ('id', 'description', 'fktype')
    list_filter = ('fktype', )