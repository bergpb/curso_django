from django.shortcuts import render, redirect
from .models import Transacao
from .forms import TransacaoForm
import datetime


def home(request):
    return render(request, 'contas/home.html')


def new(request):
    # se for um post manda pro form se não cria ele vazio
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    return render(request, 'contas/form.html', {'form': form})


def list(request):
    transacao = Transacao.objects.all()
    return render(request, 'contas/list.html', {'transacao': transacao})


def update(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    # inicia o form com o objeto do banco
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_list')

    return render(request, 'contas/form.html', {'form': form, 'transacao': transacao})


def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_list')
