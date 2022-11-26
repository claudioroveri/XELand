from django.db import models

class Palestrante(models.Model):
    nome = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=50)
    ativo = models.BooleanField(default=True) 