from django.db import models

class TipoEvento(models.Model):
    descricao = models.CharField(max_length=50, null=False)
    ativo = models.BooleanField(default=True)

