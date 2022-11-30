#JWT:  Criação de Viewsets (parte 5)
from rest_framework.permissions import IsAuthenticated
from rest.serializers import  LocalSerializer
from app.model.Local import Local
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .serializers import MyTokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import  redirect
import requests



# View para chamadas REST
class LocalViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LocalSerializer
    queryset = Local.objects.all()
   
class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.session['token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

# Parei aqui !!
def Logout(request):
    request.session['token'] = ""
    request.session['username'] = ""
    return redirect('/')
