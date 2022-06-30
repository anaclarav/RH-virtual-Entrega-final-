from django.db import models
from django.contrib.auth import get_user_model
from categoria.models import categoria
# ACRESCENTAR DEPOIS ESPAÇO PARA O ARQUIVO DE CURRICULO, EMAIL E IMAGEM PARA O PERFIL

class perfil(models.Model):

    GENEROS = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )

    TIPOS = (
        ('Trabalhador', 'Trabalhador'),
        ('Cliente', 'Cliente')
    )

    nome = models.CharField(max_length = 100, blank=False, null=True)
    sobrenome = models.CharField(max_length = 200, blank=False, null=True)
    email = models.EmailField(max_length=256, blank=False, null=True)
    CPF = models.CharField(max_length=11, blank=False, null=True)
    genero = models.CharField(
        max_length = 1, 
        choices = GENEROS,
        blank=False,
        null=True
    )
    cep = models.CharField(max_length=8, blank=False, null=True)
    rua = models.CharField(max_length=300, blank=False, null=True)
    numero = models.CharField(max_length=10, blank=False, null=True)
    bairro = models.CharField(max_length=300, blank=False, null=True)
    data_nasc = models.DateField(blank=False, null=True)
    telefone = models.CharField(max_length=15, blank=False, null=True)
    categoria = models.ForeignKey(categoria, on_delete=models.PROTECT, related_name='Categoria')
    tipo_usuario = models.CharField(
        max_length = 50, 
        choices = TIPOS,
        blank=False,
        null=True,
        default = 'Trabalhador'
    )
    detalhes = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='static/imagens_perfil/', null=True, blank=False)
    curriculo = models.FileField(upload_to='static/curriculos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True, null=True)
    updated_at = models.DateTimeField(auto_now = True, null=True)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nome + ' ' + self.sobrenome)
