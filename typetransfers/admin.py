from django.contrib import admin
from .models import TypeTransfer
# Register your models here.

@admin.register(TypeTransfer)
class AdminTypeTransfer(admin.ModelAdmin):
    list_display = ('id', 'destypetransfer', )
    list_filter = ('id', )