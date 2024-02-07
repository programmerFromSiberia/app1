from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404, render

from goods.models import Products
from goods.utils import q_search 


def catalog(request, category_slug=None):  # каталог
    
    page = request.GET.get("page", 1)  # получаем текущую страницу
    on_sale = request.GET.get("on_sale", None)  # обращаемся в каталог к кнопке "Товары по акции" "checkbox"
    order_by = request.GET.get("order_by", None)  # обращаемся в каталог к кнопке "Сортировать" "radio"
    query = request.GET.get("q", None)  # получаем поисковый запрос
    
    
    if category_slug == "all":
        goods = Products.objects.all()  # отображаем все продукты
    elif query:
        goods = q_search(query) # отображаем продукты по поисковому запросу
    else:
        goods = get_list_or_404(Products.objects.filter (category__slug=category_slug)) # отображаем продукты по категориям category_slug если продукта нет возвращаем get_list_or_404 
    
    if on_sale:
        goods = goods.filter(discount__gt=0)
        
    if order_by and order_by != "default":
        goods = goods.order_by(order_by) 
   
        
    paginator = Paginator(goods, 3) # пагинатор 3 продукта на странице
    current_page = paginator.page(int(page)) # текущая страница
    
    context = {
        "title": "VIA - Каталог", # заголовок страницы
         "goods": current_page, # отображаем текущую страницу
         "slug_url": category_slug  # slug категории
   
    }
    return render(request, "goods/catalog.html", context) # отображаем каталог


def product(request, product_slug):
    
    product = Products.objects.get(slug=product_slug) # отображаем продукт по слагу
    
    context = {"product": product}  
        
    return render(request, "goods/product.html", context=context)
