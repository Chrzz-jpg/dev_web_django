from django.http import HttpResponse
# Create your views here.

def pagina_produtos(request):
    return HttpResponse("Página de produtos")
