from django.contrib import admin
from .models import Funder
# Register your models here.

@admin.register(Funder)
class AdminFunder(admin.ModelAdmin):
    list_display = ('id', 'fundername', )
    list_filter = ('id', )