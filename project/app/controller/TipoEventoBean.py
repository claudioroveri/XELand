from django.forms import ModelForm
from app.model.TipoEvento import TipoEvento

# Aqui são criados os Beans para os formularios
class TipoEventoBean(ModelForm):
    class Meta:
        model = TipoEvento
        fields = ['id','descricao', 'ativo']