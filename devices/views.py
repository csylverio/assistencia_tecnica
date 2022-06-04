from django.urls import reverse_lazy
from django.views import generic
from .models import Device


class DeviceListView(generic.ListView):
    model: Device
    queryset = Device.objects.all()
    template_name = 'devices/device_list.html'
    
    
class DeviceDetailView(generic.DetailView):
    model = Device
    template_name = 'devices/device_detail.html'
 
    
class DeviceCreate(generic.CreateView):
    model = Device
    fields = ['model', 'manufacturer', 'color', 'code', 'voltage' ]
    template_name = 'devices/device_form.html'


class DeviceUpdate(generic.UpdateView):
    model = Device
    fields = ['model', 'manufacturer', 'color', 'code', 'voltage' ]
    template_name = 'devices/device_form.html'


class DeviceDelete(generic.DeleteView):
    model = Device
    template_name = 'devices/device_delete.html'
    success_url = reverse_lazy('devices:devices')