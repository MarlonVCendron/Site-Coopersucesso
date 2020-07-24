from django.shortcuts import render
from django.http import HttpResponse
from .models import Receita
from .models import Produto

# Create your views here.
def homepage(request):
    return render(
        request=request,
        template_name='main/home.html',
        context = {
            "produtos":Produto.objects.all,
            "receitas":Receita.objects.all
        }
    )


def receita(request, receita_id):
    return render(
        request=request,
        template_name='main/receita.html',
        context={'r': Receita.objects.get(pk=receita_id)}
    )
