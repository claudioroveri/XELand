# JWT: Serializer para autenticação JWT (parte 3)
from rest_framework import serializers
from app.model.Local import Local
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# Beans especificos para chamada REST
class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = ['id','sigla', 'descricao', 'capacidade','ativo', 'tipo']

# JWT : Classe responsável por obter o token
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token