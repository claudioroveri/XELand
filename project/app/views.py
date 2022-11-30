from django.shortcuts import render, redirect
from app.controller.TipoEventoBean import TipoEventoBean
from app.controller.EventoBean import EventoBean
from app.controller.PalestranteBean import PalestranteBean
from app.controller.LocalBean import LocalBean
from app.controller.InscritoBean import InscritoBean
from app.controller.UsuarioBean import UsuarioBean
from app.model.Palestrante import Palestrante
from app.model.TipoEvento import TipoEvento
from app.model.Local import Local
from app.model.Evento import Evento
from app.model.Inscrito import Inscrito
import requests
from rest.serializers import (MyTokenObtainPairSerializer)
from django.contrib.auth.models import User
from rest_framework_simplejwt.backends import TokenBackend



# View principal
def Principal(request):
    return render(request, 'index.html', {})

# foi criado um html customizado para criacao de usuario
# na tabela de controle de usuario de sessao do django
def UsuarioForm(request):
    data = {}
    data['form'] = UsuarioBean
    return render(request, 'formUsuario.html', data)

# Carregamento dos forms
def TipoEventoForm(request):
    data = {}
    data['form'] = TipoEventoBean
    return render(request, 'formTipoEvento.html', data)

def EventoForm(request):
    data = {}
    data['form'] = EventoBean
    data['comboPalestrante'] = Palestrante.objects.all()
    data['comboTipo'] = TipoEvento.objects.all()
    data['comboLocal'] = Local.objects.all()
    return render(request, 'formEvento.html', data)

def PalestranteForm(request):
    data = {}
    data['form'] = PalestranteBean
    return render(request, 'formPalestrante.html', data)

def LocalForm(request):
     data = {}
     data['form'] = LocalBean
     return render(request, 'formLocal.html', data)

def InscricaoForm(request, pk):
     data = {}
     data['form'] = InscritoBean
     data['evento'] = Evento.objects.get(pk=pk)
     return render(request, 'formInscricao.html', data)

# Views de criação de registros
def EventoAdd(request):
    form = EventoBean(request.POST or None)  

    if form.is_valid():
        form.save()
        return redirect('EventoForm')
    else:
        print(form.errors)
        
# Views de criação de registros
def LocalAdd(request):
    form = LocalBean(request.POST or None)  

    if form.is_valid():
        form.save()
        return redirect('LocalForm')
    else:
        print(form.errors)

# Views de criação de registros
def PalestranteAdd(request):
    form = PalestranteBean(request.POST or None)  

    if form.is_valid():
        form.save()
        return redirect('PalestranteForm')
    else:
        print(form.errors)

# Views de criação de registros
def InscricaoAdd(request):
    #Validar ainda quando usuario tenta se inscrever mais de uma vez !!!
    form = InscritoBean(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('ProgramacaoList')
    else:
        print(form.errors)

# Views de listagens
def ProgramacaoList(request):
        lista = []
        dados = Evento.objects.filter(ativo=True).all()

        for item in dados:
            inscritos = Inscrito.objects.filter(evento=item.id).count()
            linha = {}
            linha['titulo'] = item.titulo
            linha['descricao'] = item.descricao
            linha['palestrante'] = item.palestrante.nome
            linha['horario_ini'] = item.horario_inicio
            linha['horario_fim'] = item.horario_fim
            linha['vagas'] = item.vagas - inscritos
            linha['local'] = item.local.sigla
            linha['tipo'] = item.tipo.descricao
            linha['id'] = item.id
            lista.append(linha) # só exibe o ultimo

        data = {}
        data['lista'] = lista
        
        return render(request, 'Programacao.html', data)

# Utilizando autorização por token
def EventoList(request): 
    data = {}
    data['lista'] = Evento.objects.all()

    return render(request, 'listaEvento.html', data)

def InscritoList(request, pk): 
    data = {}
    data['lista'] = Inscrito.objects.filter(evento=pk).all()
    data['evento'] = Evento.objects.filter(id=pk).get()

    return render(request, 'listaInscrito.html', data)


def LocalList(request):
    data = {}
    data['lista'] = Local.objects.all()

    url = 'http://localhost:8000/LocalREST/'
    valor_token = 'Bearer ' + request.session['token']
    token = {'Authorization': valor_token}
    r = requests.get(url, headers=token)
    data['lista'] = r.json()

    return render(request, 'listaLocal.html', data)


def PalestranteList(request):
    data = {}
    data['lista'] = Palestrante.objects.all()

    return render(request, 'listaPalestrante.html', data)

#Views de deleção de registros
def EventoDelete(request, pk):
    data = Evento.objects.get(pk=pk)
    data.delete()
    return redirect('/Evento/')


def InscritoDelete(request, pk):
    data = Inscrito.objects.get(pk=pk)
    data.delete()
    return redirect('/Evento/')


def PalestranteDelete(request, pk):
    data = Palestrante.objects.get(pk=pk)
    data.delete()
    return redirect('/Palestrante/')

# Views de telas de edição
def EventoEdit(request, pk):
    data = {}
    data['item'] = Evento.objects.get(pk=pk)
    data['form'] = EventoBean(instance=data['item'])

    data['comboPalestrante'] = Palestrante.objects.all()
    data['comboTipo'] = TipoEvento.objects.all()
    data['comboLocal'] = Local.objects.all()

    return render(request, 'formEvento.html', data)

def PalestranteEdit(request, pk):
    data = {}
    data['item'] = Palestrante.objects.get(pk=pk)
    data['form'] = PalestranteBean(instance=data['item'])

    return render(request, 'formPalestrante.html', data)

def LocalEdit(request, pk):
    data = {}
    data['item'] = Local.objects.get(pk=pk)
    data['form'] = LocalBean(instance=data['item'])

    return render(request, 'formLocal.html', data)

#View de operação de edição
def EventoUpdate(request, pk):
    data = {}
    data['db'] = Evento.objects.get(pk=pk)
    form = EventoBean(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('/Evento/')
    else:
        print(form.errors)

def PalestranteUpdate(request, pk):
    data = {}
    data['db'] = Palestrante.objects.get(pk=pk)
    form = PalestranteBean(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('/Palestrante/')
    else:
        print(form.errors)

def LocalUpdate(request, pk):
    data = {}
    data['db'] = Local.objects.get(pk=pk)
    form = LocalBean(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('/Local/')
    else:
        print(form.errors)

# Outras operações
def TokenAtivo(request):
        token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        data = {'token': token}
  
        valid_data = TokenBackend(algorithm='HS256').decode(token,verify=True)
        user = valid_data['user']
        print(user)
        return redirect('/')
 

def ValidaLogin(request):
    
    input_data = {'username': request.POST.get('username'),
            'password': request.POST.get('password') }

    # Vindo de uma API REST via requisição POST
    r = requests.post("http://localhost:8000/login/", json = input_data)
    request.session['username'] = request.POST.get('username')
    request.session['token'] = r.json()['access']
    data = {}

    # Armazena o username e seu respectivo token
    # Continuar aqui !!!!
    request.session['usuario_id'] = User.objects.filter(username=request.session['username']).get().pk
    data['usuario'] = request.session['username']
    data['usuario_id'] = request.session['usuario_id']
    data['token'] = request.session['token']

    # Caso logue com sucesso
    if r.status_code == 200:
       return render(request, 'index.html', data)
    else:
       return redirect('/Usuario/login/')




