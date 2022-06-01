from django.shortcuts import render
from django.http import HttpResponse

def index_page(request):
      context = {'hello_word': 'Hello Django'}
      return render(request, 'base/index.html', context)