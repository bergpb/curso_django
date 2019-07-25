from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserResgiterForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserResgiterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Usuário {} registrado! Realize login.'.format(username))
            return redirect('login')
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
    else:           
        form = UserResgiterForm()
    return render(request, 'users/register.html', {'form':form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
