from django.db import models
from perfil.models import perfil
from cliente.models import cliente
# ACRESCENTAR DEPOIS ESPAÇO PARA O ARQUIVO DE CURRICULO, EMAIL E IMAGEM PARA O PERFIL

class contrato(models.Model):
    STATUS_CONTRATO = (
        ('Em aberto', 'Em aberto'),
        ('Finalizado', 'Finalizado'), 
        ('Cancelado', 'Cancelado')
    )
    AVALIAÇAO = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3), 
        (4, 4),
        (5, 5)
    )
    titulo = models.CharField(max_length=500, blank=False, null=True)
    detalhes_contrato = models.CharField(max_length = 10000, blank=False, null=True)
    Avaliação_trabalhador = models.IntegerField(
        choices = AVALIAÇAO,
        blank=True,
        null=False,
        default = 0,
    )
    avaliação_escrita = models.CharField(max_length = 500000, blank= True)
    status_contrato = models.CharField(max_length=100, choices=STATUS_CONTRATO, blank=False, null= True)
    created_at = models.DateTimeField(auto_now_add = True, null=True)
    updated_at = models.DateTimeField(auto_now = True, null=True)
    trabalhador = models.ForeignKey(perfil, on_delete=models.PROTECT, related_name='Trabalhador')
    cliente = models.ForeignKey(cliente, on_delete=models.PROTECT, related_name='Cliente')
