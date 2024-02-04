from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render

from goods.models import Products 


def catalog(request, category_slug, page=1,):  # каталог
    
    if category_slug == "all":
        goods = Products.objects.all()  # отображаем все продукты
    else:
        goods = get_list_or_404(Products.objects.filter (category__slug=category_slug)) # отображаем продукты по категориям category_slug если продукта нет возвращаем get_list_or_404 
        
    paginator = Paginator(goods, 3) # пагинатор 3 продукта на странице
    current_page = paginator.page(page) # текущая страница
    
    context = {
        "title": "VIA - Каталог", # заголовок страницы
         "goods": current_page, # отображаем текущую страницу
         "slug_url": category_slug
   
    }
    return render(request, "goods/catalog.html", context) 


def product(request, product_slug):
    
    product = Products.objects.get(slug=product_slug) # отображаем продукт по слагу
    
    context: dict = {"product": product}
    
    return render(request, "goods/product.html", context=context)
