from django.contrib import admin
from .models import Provider
# Register your models here.

@admin.register(Provider)
class AdminProvider(admin.ModelAdmin):
    list_display = ('id', 'provname', 'phone', 'direction')
    list_filter = ('id', )