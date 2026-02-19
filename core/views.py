
from .models import Produto,Cliente
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Cliente
def index(request):
    context = {'curso': 'Desenvolvimento de Sistemas'}
    return render(request, 'index.html', context)

def contato(request):
    context = {
        'nome': 'IFSC',
        'telefone': '(47) 3333-5555',
        'email': 'contato@ifsc.edu.br'
    }
    return render(request, 'contato.html', context)

def produtos(request):
    produtos = Produto.objects.all()
    context = {'prod': produtos}
    return render(request, 'produtos.html', context)

def clientes(request):
    clientes = Cliente.objects.all()
    context = {'cli': clientes}
    return render(request, 'clientes.html', context)

def cadastraClientes(request):
    return render(request, 'cadastraClientes.html')
    
def salvaClientes(request):
    if request.method == "POST":
        thisNome = request.POST.get('nome')
        thisSobrenome = request.POST.get('sobrenome')
        thisEmail = request.POST.get('email')
        thisCpf = request.POST.get('cpf')
        thisTelefone = request.POST.get('telefone')

        cliente = Cliente(
            nome=thisNome,
            sobrenome=thisSobrenome,
            email=thisEmail,
            cpf=thisCpf,
            telefone=thisTelefone
        )

        cliente.save()

        return redirect('urlclientes')
