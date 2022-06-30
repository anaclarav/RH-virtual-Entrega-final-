from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import contratoForm
from .models import contrato
from cliente.models import cliente 
from perfil.models import perfil

# Create your views here.
@login_required
def criar(request, id_trabalhador):
    usuario = request.user
    a = get_object_or_404(cliente, user=usuario)
    if request.method =='POST':
        form = contratoForm(request.POST)
        usuario = request.user
        c = get_object_or_404(cliente, user=usuario)
        p = get_object_or_404(perfil, pk=id_trabalhador)
        if form.is_valid():
            contrato = form.save(commit=False)
            contrato.cliente = c
            contrato.trabalhador = p
            contrato.status_contrato = 'Em aberto'
            contrato.save()
            return redirect('/')
    else:
        form = contratoForm
        return render(request, 'novoContrato.html', {'form': form, 'a': a})

def listar(request):

    usuario = request.user
    p = perfil.objects.filter(user=usuario)
    c = cliente.objects.filter(user=usuario)
    
    stt_contrato = request.GET.get('status_contrato')
    if c:
        c = get_object_or_404(cliente, user=usuario)
        if stt_contrato:
            Contrato = contrato.objects.filter(cliente=c, status_contrato=stt_contrato)  
        else:
            Contrato = contrato.objects.filter(cliente=c)

        return render(request, 'listarContrato-cliente.html', {'Contrato': Contrato, 'a': c})
    else:
        p = get_object_or_404(perfil, user=usuario)
        if stt_contrato:
            Contrato = contrato.objects.filter(trabalhador=p, status_contrato=stt_contrato)  
        else:
            Contrato = contrato.objects.filter(trabalhador=p)

        return render(request, 'listarContrato-trabalhador.html', {'Contrato': Contrato, 'a': p})
    

@login_required
def detail(request, id):
    usuario = request.user
    p = perfil.objects.filter(user=usuario)
    c = cliente.objects.filter(user=usuario)
    Contrato = get_object_or_404(contrato, pk=id)
    if p:
        a = get_object_or_404(perfil, user=usuario)
        return render(request, 'detalhesContrato-trabalhador.html', {'Contrato': Contrato, 'a':a})
    else:
        a = get_object_or_404(cliente, user=usuario)
        return render(request, 'detalhesContrato-cliente.html', {'Contrato': Contrato, 'a':a})

@login_required
def editar(request, id):
    usuario = request.user
    a = get_object_or_404(cliente, user=usuario)
    Contrato = get_object_or_404(contrato, pk=id)
    form = contratoForm(instance=Contrato)

    if request.method == 'POST':
        form = contratoForm(request.POST, instance=Contrato)

        if form.is_valid():
            Contrato.save()
            return redirect('/')
        else:
            return render(request, 'editarContrato.html', {'form': form, 'Contrato': Contrato, 'a': a})   
    
    else:
        return render(request, 'editarContrato.html', {'form': form, 'Contrato': Contrato, 'a':a})

def cancelar(request, id):
    Contrato = get_object_or_404(contrato, pk=id)
    Contrato.status_contrato = 'Cancelado'
    Contrato.save()

    return redirect('/contrato/listar/')

def finalizar(request, id):
    Contrato = get_object_or_404(contrato, pk=id)
    Contrato.status_contrato = 'Finalizado'
    Contrato.save()

    return redirect('/contrato/listar/')
