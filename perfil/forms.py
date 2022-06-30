from django import forms 
from .models import perfil

class perfilForm (forms.ModelForm):
    class Meta:
        model= perfil
        fields = ('nome', 'sobrenome', 'CPF', 'genero', 'cep', 'rua', 'numero', 'bairro', 'data_nasc', 'telefone', 'detalhes', 'categoria','curriculo', 'imagem')

class perfilEditarForm (forms.ModelForm):
    class Meta:
        model= perfil
        fields = ('nome', 'sobrenome', 'CPF', 'genero', 'cep', 'rua', 'numero', 'bairro', 'telefone', 'detalhes', 'categoria','curriculo', 'imagem')