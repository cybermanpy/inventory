from django.contrib import admin
from .models import Brand
# Register your models here.

@admin.register(Brand)
class AdminBrand(admin.ModelAdmin):
    list_display = ('id', 'brandname', )
    list_filter = ('id', )