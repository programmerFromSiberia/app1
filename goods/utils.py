from django.db.models import Q

from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline,
)
from goods.models import Products

def q_search(query):  # поиск по поисковому запросу

    if (
        query.isdigit() and len(query) <= 5
    ):  # если поисковый запрос состоит из цифр и длина меньше или = 5 символов
        return Products.objects.filter(id=int(query))  # отображаем продукт по id

    # поисковик Джанго из коробки https://docs.djangoproject.com/en/5.0/ref/contrib/postgres/search/

    vector = SearchVector("name", "description") # Создаем вектор для поиска
    query = SearchQuery(query) # создаем запрос

    result = (
        Products.objects.annotate(rank=SearchRank(vector, query)) 
        .filter(rank__gt=0)
        .order_by("-rank")
    ) # Фильтруем чтобы ранг был  больше 0 и сортируем по рангу
    
    
    
# Формируем запросы для поиска

    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel='<span style="background-color: yellow;">', # формируем выделение для названия
            stop_sel="</span>", # закрываем тег span 
        )
    ) # поиск по названию

    result = result.annotate(
        bodyline=SearchHeadline(
            "description",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )  # поиск по описанию
    
    return result  # возвращаем результат
    
    
    
    

    # keywords = [word for word in query.split() if len(word) > 2]  # список ключевых слов
    # q_objects = Q()

    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)  # поиск по ключевым словам в описании товара
    #     q_objects |= Q(name__icontains=token)  # поиск по ключевым словам в названии товара

    # return Products.objects.filter(q_objects)
