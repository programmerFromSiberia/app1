from django.shortcuts import render

def login(request):
    context = {
        'title': 'VIA - Авторизация'
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'VIA - Регистрация'
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'VIA - Кабинет'
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    ...
