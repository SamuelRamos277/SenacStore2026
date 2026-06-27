from django.shortcuts import render
from StoreApp.models import Departamento

# Create your views here.

def index(request):
    departamentos = Departamento.objects.all()

    context = {
        'departamentos': departamentos}
    
    return render(request, 'index.html', context)

def departamentos(request):
    return render(request, 'produtos.html', {})
