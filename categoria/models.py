from django.db import models

# Create your models here.
class categoria(models.Model):
    nome = models.CharField(max_length = 1000, blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add = True, null=True)
    updated_at = models.DateTimeField(auto_now = True, null=True)

    def __str__(self):
        return str(self.nome)