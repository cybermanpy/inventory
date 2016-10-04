from django.contrib import admin
from .models import Direction

# Register your models here.

@admin.register(Direction)
class AdminDirection(admin.ModelAdmin):
    list_display = ('id', 'acronym', 'dirname', 'dirnumber')
    list_filter = ('dirname', )