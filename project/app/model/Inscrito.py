from django.db import models
from app.model.Evento import Evento

class Inscrito(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    idade = models.IntegerField()
    evento = models.ManyToManyField(Evento)