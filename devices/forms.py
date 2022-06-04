from django.forms import ModelForm
from .models import Device


class DeviceModelForm(ModelForm):
    model = Device
    fields = ['model', 'manufacturer', 'color', 'code', 'voltage' ]