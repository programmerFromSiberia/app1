from django.db.models import Q

from goods.models import Products


def q_search(query):  # поиск по поисковому запросу
    
    if query.isdigit() and len(query) <= 5: # если поисковый запрос состоит из цифр и длина меньше 5 символов
       return Products.objects.filter(id=int(query))  # отображаем продукт по id
   
    keywords = [word for word in query.split() if len(word) > 2]  # список ключевых слов
    q_objects = Q()
    
    for token in keywords:
        q_objects |= Q(description__icontains=token)  # поиск по ключевым словам в описании товара
        q_objects |= Q(name__icontains=token)  # поиск по ключевым словам в названии товара
        
    return Products.objects.filter(q_objects)
        