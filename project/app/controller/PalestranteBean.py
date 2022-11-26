from django.forms import ModelForm
from app.model.Palestrante import Palestrante

# Aqui são criados os Beans para os formularios
class PalestranteBean(ModelForm):
    class Meta:
        model = Palestrante
        fields = ['id','nome','instituicao', 'ativo']