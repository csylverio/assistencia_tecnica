from django.forms import ModelForm
from .models import Manufacturer


class ManufacturerModelForm(ModelForm):
    model = Manufacturer
    fields = ['name']