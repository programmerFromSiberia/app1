# Создаем функцию для возвращения значка категорий на все страницы

from django import template
from django.utils.http import urlencode

from goods.models import Categories

# регистрируем шаблонный тег
register = template.Library()  

@register.simple_tag   
def tag_categories():   
    return Categories.objects.all()  # возвращаем все категории

@register.simple_tag(takes_context=True) # принимает все контекстные переменные из urls.py, catalog.html
def change_params(context, **kwargs):  # принимает словарь
    query = context['request'].GET.dict()  # получаем словарь GET
    query.update(kwargs)  # обновляем словарь
    return urlencode(query)  # переводим словарь в строку