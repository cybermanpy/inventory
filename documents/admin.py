from django.contrib import admin
from .models import Document
# Register your models here.

@admin.register(Document)
class AdminDocument(admin.ModelAdmin):
    list_display = ('id', 'desdocument', )
    list_filter = ('id', )