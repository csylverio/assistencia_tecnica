from django.contrib import admin
from .models import PaymentForm, PaymentTerm


class PaymentFormAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
    
class PaymentTermAdmin(admin.ModelAdmin):
    list_display = ('name',)
    

admin.site.register(PaymentForm, PaymentFormAdmin)
admin.site.register(PaymentTerm, PaymentTermAdmin)