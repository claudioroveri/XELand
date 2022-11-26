from django.forms import ModelForm
from app.model.Inscrito import Inscrito

# Aqui são criados os Beans para os formularios
class InscritoBean(ModelForm):
    class Meta:
        model = Inscrito
        fields = ['id','nome', 'email', 'idade','evento']