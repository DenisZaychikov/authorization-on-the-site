from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import NewForm


def check(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
    else:
        form = NewForm()

    return render(request, 'check.html', {'form': form})


def login(request):
    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect(login)
        else:
            print('error_messages =', form.error_messages)
            print('errors =', form.errors)
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})
