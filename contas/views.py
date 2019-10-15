from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Transacao
from .formulario import TransacaoFormulario
import datetime


def home(request):
    data = {}


'''
    data['transacoes'] = ['t1', 't2', 't3']
    data['now'] = datetime.datetime.now()

#    html = "<html><body>It is now %s.</body></html>" % now.today()
    return render(request, 'contas/home.html', data)

'''


def listagem(request):
    dados = {'transacoes': Transacao.objects.all()}
    return render(request, 'contas/listagem.html', dados)


def nova_transacao(request):
    data = {}
    form = TransacaoFormulario(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['formulario'] = form
    return render(request, 'contas/formulario.html', data)


def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    formu = TransacaoFormulario(request.POST or None, instance=transacao)
    if formu.is_valid():
        formu.save()
        return redirect('url_listagem')

    data['formulario'] = formu
    data['transacao'] = transacao
    return render(request, 'contas/formulario.html', data)


def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')
