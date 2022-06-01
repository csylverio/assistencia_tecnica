from django.contrib import admin
from .models import Device


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'code', 'description', 'model')


admin.site.register(Device, DeviceAdmin)
