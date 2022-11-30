from django.forms import ModelForm
from django.contrib.auth.models import User

class UsuarioBean(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name','last_name', 'password']