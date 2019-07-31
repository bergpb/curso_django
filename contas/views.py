from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    gastos = 0
    transacoes = Transaction.objects.filter(user=request.user).all()
    for i in range(0, len(transacoes)):
        print(transacoes[i])
        gastos += transacoes[i].value

    return render(request, 'contas/home.html', {'gastos': gastos})


@login_required
def new(request):
    if request.method == 'POST':
        # se for um post manda pro form se não cria ele vazio
        form = TransactionForm(request.POST)

        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.user= request.user
            form_save.save()
            return redirect('url_list')
    else:
        form = TransactionForm()

    return render(request, 'contas/form.html', {'form': form})


@login_required
def list(request):
    transacoes = Transaction.objects.filter(user=request.user).order_by('-date_created')
    return render(request, 'contas/list.html', {'transacoes': transacoes})


@login_required
def update(request, pk):
    transacao = Transaction.objects.filter(pk=pk, user=request.user).first()

    if transacao:
        # inicia o form com o objeto do banco que vem no instance
        form = TransactionForm(request.POST or None, instance=transacao)

        if form.is_valid():
            # se form for válido, cria o form mas não salva, altera o valor do f.user.
            form_save = form.save(commit=False)
            form_save.user = request.user
            form_save.save()
            return redirect('url_list')

        return render(request, 'contas/form.html', {'form': form,
                                                    'transacao': transacao})
    else:
        messages.error(request, 'Transação não encontrada.')
        return redirect('url_list')


@login_required
def delete(request, pk):
    transacao = Transaction.objects.filter(pk=pk, user=request.user).first()
    if transacao:
        transacao.delete()
    else:
        messages.error(request, 'Transação não encontrada.')
        return redirect('url_list')
