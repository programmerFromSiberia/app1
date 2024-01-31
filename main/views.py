from django.http import HttpResponse
from django.shortcuts import render
from django.template import context

# Получаем доступ к ОРМ Системе а именно к Категориям
from goods.models import Categories 


# обработчик запросов (контроллеров) на главной странице сайта
def index(request):
    
    categories = Categories.objects.all()
    context = {
        'title': 'VIA - Главная',
        'content': 'Магазин мебели в стиле "Ретро" VIA',
        'categories': categories               
    }
    
    return render(request, 'main/index.html', context) # главная страница

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': "Наша компания с 2009 года успешно занимается поставкой мебели для дома, офиса и дачи, мы работаем напрямую с ведущими Российскими производителями и поставщиками мебели и аксессуаров. Для вас мы предлагаем мебель более 100 мебельных фабрик, расположенных в разных регионах России. Изделия данных фабрик проверены временем и пользуются заслуженной любовью покупателей. Мы понимаем, как важно для вас получить действительно качественное изделие по доступной цене и стремимся поддерживать цены строго в пределах, рекомендованных производителем, а зачастую и ниже."      
    }
    
    return render(request, 'main/about.html', context)


