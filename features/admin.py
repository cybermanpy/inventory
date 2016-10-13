from django.contrib import admin
from .models import Feature
# Register your models here.

@admin.register(Feature)
class AdminFeature(admin.ModelAdmin):
    list_display = ('id', 'desfeature')
    list_filter = ('id', )