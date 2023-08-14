from django.contrib import admin
from .models import vehicleDB
# Register your models here.

@admin.register(vehicleDB)
class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ['id','Vehicle_Number','Vehicle_Type','Vehicle_Model','Description']
