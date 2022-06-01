from django.contrib import admin
from .models import Manufacturer


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Manufacturer, ManufacturerAdmin)

