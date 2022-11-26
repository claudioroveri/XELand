from django.forms import ModelForm
from app.model.Evento import Evento

# Aqui são criados os Beans para os formularios
class EventoBean(ModelForm):
    class Meta:
        model = Evento
        fields = ['id','titulo', 'descricao', 'data', 'horario_inicio', 'horario_fim','vagas', 'palestrante', 'tipo', 'local', 'ativo']