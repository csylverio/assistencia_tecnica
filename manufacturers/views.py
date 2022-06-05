from django.urls import reverse_lazy
from django.views import generic
from .models import Manufacturer


class ManufacturerListView(generic.ListView):
    model: Manufacturer
    queryset = Manufacturer.objects.all()
    template_name = 'manufacturers/manufacturer_list.html'
    
    
class ManufacturerDetailView(generic.DetailView):
    model = Manufacturer
    template_name = 'manufacturers/manufacturer_detail.html'
 
    
class ManufacturerCreate(generic.CreateView):
    model = Manufacturer
    fields = ['name']
    template_name = 'manufacturers/manufacturer_form.html'
    
    
class ManufacturerUpdate(generic.UpdateView):
    model = Manufacturer
    fields = ['name']
    template_name = 'manufacturers/manufacturer_form.html'


class ManufacturerDelete(generic.DeleteView):
    model = Manufacturer
    template_name = 'manufacturers/manufacturer_delete.html'
    success_url = reverse_lazy('manufacturers:manufacturers')