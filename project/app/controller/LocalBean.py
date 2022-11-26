from django.forms import ModelForm
from app.model.Local import Local

# Aqui são criados os Beans para os formularios
class LocalBean(ModelForm):
    class Meta:
        model = Local
        fields = ['id','sigla', 'descricao', 'capacidade','ativo', 'tipo']