from django.urls import reverse
from django.db import models


class Manufacturer(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name =  models.CharField(max_length=50, blank=False, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse('manufacturers:manufacturer-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.name
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Manufacturer._meta.fields]
    
    class Meta:
        ordering = ['name']