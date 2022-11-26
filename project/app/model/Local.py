from django.db import models

class Local(models.Model):
    tipo = models.CharField(max_length=50, default="")
    descricao = models.CharField(max_length=100, default="")
    sigla = models.CharField(max_length=5)
    capacidade = models.IntegerField(default=50)
    ativo = models.BooleanField(default=True) 