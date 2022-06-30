from django import forms 
from .models import cliente

class clienteForm (forms.ModelForm):
    class Meta:
        model= cliente
        fields = ('nome', 'sobrenome', 'cep', 'rua', 'numero', 'bairro', 'telefone', 'imagem')