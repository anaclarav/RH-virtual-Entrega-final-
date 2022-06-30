from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from .forms import perfilForm, perfilEditarForm
from .models import perfil
from cliente.models import cliente 
from categoria.models import categoria
from contrato.models import contrato
from users.views import tipoUsuario
import os 
# Create your views here

@login_required
def home(request):
    usuario = request.user
    p = perfil.objects.filter(user=usuario)
    c = cliente.objects.filter(user=usuario)
    a = 0
    if p:
        a = get_object_or_404(perfil, user=usuario)
        return render(request, 'home-trabalhador.html', {'a': a, 'c': c, 'p': p})
    elif c:
        a = get_object_or_404(cliente, user=usuario)
        return render(request, 'home-cliente.html', {'a': a, 'c': c, 'p': p})
    else:
        return redirect(reverse('tipoUsuario'))


@login_required
def detail(request, id):
    usuario = request.user
    a = get_object_or_404(cliente, user=usuario)
    Perfil = get_object_or_404(perfil, pk=id)
    Contrato = contrato.objects.filter(trabalhador=Perfil)
    soma = 0
    cont = 0
    for i in Contrato:
        if i.Avaliação_trabalhador != 0 : 
            soma = soma + i.Avaliação_trabalhador
            cont = cont + 1
    if cont != 0:
        media_avaliaçao = soma/cont
    else:
        media_avaliaçao = 0
    return render(request, 'visualizaçaoPerfil.html', {'perfil': Perfil, 'media':media_avaliaçao, 'quant_trab': cont, 'a':a})


@login_required
def meuperfil(request, id):
    Perfil = get_object_or_404(perfil, pk=id)
    Contrato = contrato.objects.filter(trabalhador=Perfil)
    soma = 0
    cont = 0
    for i in Contrato:
        if i.Avaliação_trabalhador != 0 : 
            soma = soma + i.Avaliação_trabalhador
            cont = cont + 1
    if cont != 0:
        media_avaliaçao = soma/cont
    else:
        media_avaliaçao = 0
    return render(request, 'visualizaçaoMeuPerfil.html', {'perfil': Perfil, 'media':media_avaliaçao, 'quant_trab': cont, 'a': Perfil})

@login_required
def listar(request):
    usuario = request.user
    a = get_object_or_404(cliente, user=usuario)

    search = request.GET.get('search')

    if search:
        categ = categoria.objects.filter(nome__icontains=search)
        if categ:
            c = get_object_or_404(categoria, nome__icontains=search)
            Perfil = perfil.objects.filter(categoria=c)
        else:
            Perfil = 0
    else:
        Perfil = perfil.objects.all()

    context={
        'perfil': Perfil,
        'a' : a,
    }
    return render(request, 'listar.html', context)

@login_required
def criar(request):
    categorias = categoria.objects.all()
    if request.method =='POST':
        form = perfilForm(request.POST, request.FILES)
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.user = request.user
            perfil.save()
            return redirect('/')
        else:
             return render(request, 'novoPerfil.html', {'form': form, 'categoria':categorias})
    else:
        form = perfilForm
        return render(request, 'novoPerfil.html', {'form': form, 'categoria':categorias})

@login_required
def editar(request, id):
    Perfil = get_object_or_404(perfil, pk=id)
    form = perfilEditarForm(instance=Perfil)
    categorias = categoria.objects.all()

    if request.method == 'POST':
        form = perfilEditarForm(request.POST, request.FILES, instance=Perfil)
        
        aa = request.POST.get('curriculo', False)
        ab = request.POST.get('imagem', False)

        if aa:
            if len(Perfil.curriculo) > 0:
                os.remove(Perfil.curriculo.path)
            Perfil.curriculo = request.FILES['curriculo']

        if ab:
            if len(Perfil.imagem) > 0:
                os.remove(Perfil.imagem.path)
            Perfil.imagem = request.FILES['imagem']

        if form.is_valid():
            Perfil.save()
            return redirect('/')
        else:
            return render(request, 'editarPerfil.html', {'form': form, 'perfil': Perfil, 'a':Perfil})   
    
    else:
        return render(request, 'editarPerfil.html', {'form': form, 'perfil': Perfil, 'categoria':categorias, 'a':Perfil})


@login_required
def deletar(request, id):
    perfil.objects.get(pk=id).delete()
    return redirect('/')

@login_required
def avaliaçoes(request, id):
    usuario = request.user
    c = cliente.objects.filter(user=usuario)
    if c:
        a = get_object_or_404(cliente, user=usuario)


    p = get_object_or_404(perfil, pk=id)
    contratos = contrato.objects.filter(trabalhador=p)

    soma = 0
    cont = 0
    for i in contratos:
        if i.Avaliação_trabalhador != 0 : 
            soma = soma + i.Avaliação_trabalhador
            cont = cont + 1
    if cont != 0:
        media_avaliaçao = soma/cont
    else:
        media_avaliaçao = 0
    
    if c:
        return render(request, 'listaAvaliaçoes.html', {'contrato': contratos, 'perfil':p, 'media':media_avaliaçao, 'quant_trab': cont, 'a':a} )
    else:
        return render(request, 'minhasAvaliaçoes.html', {'contrato': contratos, 'perfil':p, 'media':media_avaliaçao, 'quant_trab': cont, 'a':p} )