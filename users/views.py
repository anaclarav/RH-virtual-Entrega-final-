from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic

class cadastro(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'cadastro.html'


def tipoUsuario(request):
    tipo = request.GET.get('tipo')
    if tipo:
        if tipo=='c':
            return redirect('/perfil-cliente/criar/')
        else:
            return redirect('/perfil-trabalhador/criar/')
    else:
        return render(request, 'tipoUsuario.html')