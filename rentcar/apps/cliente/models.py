from django.db import models

class Cliente(models.Model):
    nome = models.CharField("Nome Completo", max_length=100)
    cpf = models.CharField("CPF", max_length=11, unique=True)
    cnh = models.CharField("CNH", max_length=20, unique=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering =['id']
    
    def __str__(self):
        return self.name