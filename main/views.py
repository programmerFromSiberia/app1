from django.http import HttpResponse
from django.shortcuts import render
from django.template import context

# обработчик запросов (контроллеров) на главной странице сайта
def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница магазина - Home',
        'list': ['first', 'second'],
        'dict': {'first', 1},
        'is_authenticated': False        
    }
    
    return render(request, 'main/index.html', context) # главная страница

def about(request):
    return HttpResponse('About page')


