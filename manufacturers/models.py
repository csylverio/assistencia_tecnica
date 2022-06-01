from django.db import models


class Manufacturer(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name =  models.CharField(max_length=150, blank=False, null=False)
            
    def __str__(self):
        return self.name