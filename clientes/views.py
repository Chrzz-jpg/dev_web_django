from django.shortcuts import render
# Create your views here.

def pagina_clientes(request):
    return render(request, 'clientes/index.html')