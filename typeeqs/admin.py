from django.contrib import admin
from .models import TypeEq

# Register your models here.

@admin.register(TypeEq)
class AdminTypeEq(admin.ModelAdmin):
	list_display = ('id', 'name', 'code', )
	list_filter = ('name', )