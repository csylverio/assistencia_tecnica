from django.urls import reverse_lazy
from django.views import generic
from .models import Client


class ClientListView(generic.ListView):
    model: Client
    queryset = Client.objects.all()
    template_name = 'clients/client_list.html'
    
    
class ClientDetailView(generic.DetailView):
    model = Client
    template_name = 'clients/client_detail.html'
 
    
class ClientCreate(generic.CreateView):
    model = Client
    fields = ['name', 'birth_date', 'type', 'rg', 'cpf', 'cnpj', 'email', 'phone_ddd', 'phone', 'celphone_ddd', 'celphone', 'contact', 'alldress', 
              'cep', 'city', 'uf' ]
    template_name = 'clients/client_form.html'


class ClientUpdate(generic.UpdateView):
    model = Client
    fields = ['name', 'birth_date', 'type', 'rg', 'cpf', 'cnpj', 'email', 'phone_ddd', 'phone', 'celphone_ddd', 'celphone', 'contact', 'alldress', 
              'cep', 'city', 'uf' ]
    template_name = 'clients/client_form.html'


class ClientDelete(generic.DeleteView):
    model = Client
    template_name = 'clients/client_delete.html'
    success_url = reverse_lazy('clients:clients')
