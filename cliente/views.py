from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import clienteForm
from .models import cliente
from perfil.models import perfil
import os 
# Create your views here.
@login_required
def criar(request):
    if request.method =='POST':
        form = clienteForm(request.POST, request.FILES)

        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.user = request.user
            cliente.save()
            return redirect('/')
        else:
            form = clienteForm
            return render(request, 'listar.html', {'form': form})
    else:
        form = clienteForm
        return render(request, 'novoCliente.html', {'form': form})

@login_required
def detail(request, id):
    Cliente = get_object_or_404(cliente, pk=id)
    usuario = request.user
    a = get_object_or_404(perfil, user=usuario)
    return render(request, 'perfilCliente.html', {'Cliente': Cliente, 'a': a})

@login_required
def meuperfil(request, id):
    usuario = request.user
    a = get_object_or_404(cliente, user=usuario)
    Cliente = get_object_or_404(cliente, pk=id)
    return render(request, 'meuperfil-Cliente.html', {'Cliente': Cliente, 'a': a})

@login_required
def editar(request, id):
    usuario = request.user
    a = get_object_or_404(cliente, user=usuario)
    Cliente = get_object_or_404(cliente, pk=id)
    form = clienteForm(instance=Cliente)

    if request.method == 'POST':
        form = clienteForm(request.POST, request.FILES, instance=Cliente)

        aa = request.POST.get('imagem', False)
        if aa:
            if len(Cliente.imagem) > 0:
                os.remove(Cliente.imagem.path)
            Cliente.imagem = request.FILES['imagem']
        if form.is_valid():
            Cliente.save()
            return redirect('/')
        else:
            return render(request, 'editarCliente.html', {'form': form, 'Cliente': Cliente,'a': a})   
    
    else:
        return render(request, 'editarCliente.html', {'form': form, 'Cliente': Cliente, 'a': a})