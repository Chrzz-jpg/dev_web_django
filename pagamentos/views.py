from django.shortcuts import render
# Create your views here.

def pagina_pagamentos(request):
    return render(request, 'pagamentos/index.html')