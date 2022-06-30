from django.db import models
from django.contrib.auth import get_user_model


class cliente(models.Model):
    TIPOS = (
        ('Trabalhador', 'Trabalhador'),
        ('Cliente', 'Cliente')
    )
    nome = models.CharField(max_length = 100, blank=False, null=True)
    sobrenome = models.CharField(max_length = 200, blank=False, null=True)
    cep = models.CharField(max_length=8, blank=False, null=True)
    rua = models.CharField(max_length=300, blank=False, null=True)
    numero = models.CharField(max_length=10, blank=False, null=True)
    bairro = models.CharField(max_length=300, blank=False, null=True)
    telefone = models.CharField(max_length=15, blank=False, null=True)
    tipo_usuario = models.CharField(
        max_length = 50, 
        choices = TIPOS,
        blank=False,
        null=True, 
        default = 'Cliente'
    )
    imagem = models.ImageField(upload_to='static/imagens_perfil/', null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add = True, null=True)
    updated_at = models.DateTimeField(auto_now = True, null=True)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nome + ' ' + self.sobrenome)