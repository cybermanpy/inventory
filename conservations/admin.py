from django.contrib import admin
from .models import Conservation

# Register your models here.
@admin.register(Conservation)
class AdminConservation(admin.ModelAdmin):
	list_display = ('id', 'description')
	list_filter = ('description',)