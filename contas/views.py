from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'contas/home.html')


@login_required
def new(request):
    # se for um post manda pro form se não cria ele vazio
    form = TransactionForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_list')

    return render(request, 'contas/form.html', {'form': form})


@login_required
def list(request):
    transacoes = Transaction.objects.all()
    return render(request, 'contas/list.html', {'transacoes': transacoes})


@login_required
def update(request, pk):
    transacao = Transaction.objects.get(pk=pk)
    # inicia o form com o objeto do banco
    form = TransactionForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_list')

    return render(request, 'contas/form.html', {'form': form,
                                                'transacao': transacao})


@login_required
def delete(request, pk):
    transacao = Transaction.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_list')
