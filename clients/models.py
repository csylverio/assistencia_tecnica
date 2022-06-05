from django.urls import reverse
from django.db import models
#from manufacturers.models import Manufacturer


class Client(models.Model):
    PF = 'PF'
    PJ = 'PJ'
    
    TYPE_CHOICES = (
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica')
    )
    
    UF_CHOICES = (
        ('RO', 'Rondônia'),
        ('AC', 'Acre'),
        ('AM', 'Amazonas'),
        ('RR', 'Roraima'),
        ('PA', 'Pará'),
        ('AP', 'Amapá'),
        ('TO', 'Tocantins'),
        ('MA', 'Maranhão'),
        ('PI', 'Piauí'),
        ('CE', 'Ceará'),
        ('RN', 'Rio Grande do Norte'),
        ('PB', 'Paraíba'),
        ('PE', 'Pernambuco'),
        ('AL', 'Alagoas'),
        ('SE', 'Sergipe'),
        ('BA', 'Bahia'),
        ('MG', 'Minas Gerais'),
        ('ES', 'Espírito Santo'),
        ('RJ', 'Rio de Janeiro'),
        ('SP', 'São Paulo'),
        ('PR', 'Paraná'),
        ('SC', 'Santa Catarina'),
        ('RS', 'Rio Grande do Sul'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('GO', 'Goiás'),
        ('DF', 'Distrito Federal')
    )

    name = models.CharField(max_length=100, null=False, blank=False)
    birth_date = models.DateField()
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=PF)
    rg = models.CharField(max_length=9, null=True, blank=True)
    cpf = models.CharField(max_length=11, null=True, blank=True)
    cnpj = models.CharField(max_length=14, null=True, blank=True)
    email = models.CharField(max_length=100, null=False, blank=False)
    phone_ddd = models.CharField(max_length=3, default='11', null=True, blank=True)
    phone = models.CharField(max_length=8, null=True, blank=True)
    celphone_ddd = models.CharField(max_length=3, default='11')
    celphone = models.CharField(max_length=12, null=False, blank=False)
    contact = models.CharField(max_length=150, null=False, blank=False)
    alldress = models.CharField(max_length=60, null=False, blank=False)
    cep = models.CharField(max_length=8, null=False, blank=False)
    city = models.CharField(max_length=30, null=False, blank=False)
    uf = models.CharField(max_length=2, choices=UF_CHOICES, blank=False, null=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('clients:client-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.name
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Client._meta.fields]
    
    class Meta:
        ordering = ['name']