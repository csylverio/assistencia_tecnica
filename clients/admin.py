from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'type', 'rg', 'cpf', 'cnpj', 'email',)


admin.site.register(Client, ClientAdmin)
