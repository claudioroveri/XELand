from django.db import models
from app.model.TipoEvento import TipoEvento
from app.model.Palestrante import Palestrante
from app.model.Local import Local

class Evento(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    descricao = models.CharField(max_length=200, null=False)
    data = models.DateField(null=True)
    horario_inicio = models.TimeField(null=True)
    horario_fim = models.TimeField(null=True)
    vagas = models.IntegerField(default=40)
    ativo = models.BooleanField(default=True)
    palestrante = models.ForeignKey(Palestrante, on_delete=models.PROTECT)
    tipo = models.ForeignKey(TipoEvento, on_delete=models.PROTECT)
    local = models.ForeignKey(Local, on_delete=models.PROTECT, default=1)
