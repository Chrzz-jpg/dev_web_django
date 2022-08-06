from django.shortcuts import render
# Create your views here.

def pagina_pedidos(request):
    return render(request, 'pedidos/index.html')