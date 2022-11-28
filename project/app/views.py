from django.shortcuts import render, redirect
from app.controller.TipoEventoBean import TipoEventoBean
from app.controller.EventoBean import EventoBean
from app.controller.PalestranteBean import PalestranteBean
from app.controller.LocalBean import LocalBean
from app.controller.InscritoBean import InscritoBean
from app.model.Palestrante import Palestrante
from app.model.TipoEvento import TipoEvento
from app.model.Local import Local
from app.model.Evento import Evento
from app.model.Inscrito import Inscrito
import requests


# Create your views here.
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

#Views de deleção de registros
def PalestranteDelete(request, pk):
    data = Palestrante.objects.get(pk=pk)
    data.delete()
    return redirect('/Palestrante/')

# View de edição de registros
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


