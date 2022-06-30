from django import forms 
from .models import contrato

class contratoForm (forms.ModelForm):
    class Meta:
        model= contrato
        fields = ('titulo','detalhes_contrato', 'Avaliação_trabalhador', 'avaliação_escrita')