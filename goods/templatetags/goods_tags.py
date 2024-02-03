# Создаем функцию для возвращения значка категорий на все страницы

from django import template

from goods.models import Categories

# регистрируем шаблонный тег
register = template.Library()

@register.simple_tag
def tag_categories():
    return Categories.objects.all()



