
from .models import Produto,Cliente
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Cliente
from django.shortcuts import get_object_or_404, redirect
from .models import Cliente
from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Cliente
from django.contrib.auth.decorators import login_required

@login_required
def minha_view(request):
    ...

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == "POST":
        cliente.nome = request.POST.get('nome')
        cliente.sobrenome = request.POST.get('sobrenome')

        data_nasc = request.POST.get('data_nascimento')
        if data_nasc:  
            cliente.data_nascimento = data_nasc
        else:
            cliente.data_nascimento = None
        cliente.cpf = request.POST.get('cpf')                   
        cliente.telefone = request.POST.get('telefone')
        cliente.email = request.POST.get('email')

        cliente.save()
        return redirect('urlclientes')

    return render(request, 'editar_cliente.html', {'cliente': cliente})

def excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == "POST":
        cliente.delete()

    return redirect('urlclientes')
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
    sort = request.GET.get('sort')

    if sort == 'nome_asc':
        cli = Cliente.objects.all().order_by('nome')
    elif sort == 'nome_desc':
        cli = Cliente.objects.all().order_by('-nome')
    else:
        cli = Cliente.objects.all()

    context = {'cli': cli}
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
