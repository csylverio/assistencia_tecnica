from django.db import models
from manufacturers.models import Manufacturer


class Device(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    manufacturer = models.ForeignKey(Manufacturer, null=True, on_delete=models.CASCADE)
    code = models.CharField(max_length=20, blank=False, null=False)
    description = models.CharField(max_length=50, blank=False, null=False)
    voltage = models.IntegerField(blank=False, null=False)
    model = models.CharField(max_length=50, blank=False, null=False)
    color = models.CharField(max_length=20, blank=False, null=False)
    createdat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question