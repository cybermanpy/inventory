from django.contrib import admin
from .models import Position
# Register your models here.

@admin.register(Position)
class AdminPosition(admin.ModelAdmin):
	list_display = ('id', 'description', )
	list_filter = ('description',)