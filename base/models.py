from django.db import models


# Forma de pagamento
class PaymentForm (models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name =  models.CharField(max_length=50, blank=False, null=False)
        
    def __str__(self):
        return self.name
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in PaymentForm._meta.fields]
    
    class Meta:
        ordering = ['id']
        
        
# Condições de pagamento
class PaymentTerm (models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name =  models.CharField(max_length=50, blank=False, null=False)
        
    def __str__(self):
        return self.name
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in PaymentTerm._meta.fields]
    
    class Meta:
        ordering = ['id']
