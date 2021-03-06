from django.contrib import admin
from .models import Device


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('model', 'manufacturer', 'code', 'color')


admin.site.register(Device, DeviceAdmin)
