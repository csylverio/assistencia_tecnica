from django.urls import reverse
from django.db import models


class Manufacturer(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name =  models.CharField(max_length=150, blank=False, null=False)
    
    def get_absolute_url(self):
        return reverse('manufacturers:manufacturer-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']