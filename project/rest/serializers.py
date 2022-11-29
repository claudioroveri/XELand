# JWT: Serializer para autenticação JWT (parte 3)
from rest_framework import serializers
from app.model.Evento import Evento



class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['id','titulo', 'descricao', 'data', 'horario_inicio', 'horario_fim','vagas', 'palestrante', 'tipo', 'local', 'ativo']