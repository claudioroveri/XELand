#JWT:  Criação de Viewsets (parte 5)
from rest_framework.permissions import IsAuthenticated
from rest.serializers import EventoSerializer
from app.model.Evento import Evento
from rest_framework.viewsets import ModelViewSet


class EventoViewSet(ModelViewSet):

    serializer_class = EventoSerializer
    queryset = Evento.objects.all()
    permission_classes = [IsAuthenticated]