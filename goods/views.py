from django.shortcuts import get_list_or_404, get_object_or_404, render

from goods.models import Products 


def catalog(request, category_slug):
    
    if category_slug == "all":
        goods = Products.objects.all()  # отображаем все продукты
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug)) # отображаем пустую страницу 404 если товара нет
    
       
    context = {
        "title": "VIA - Каталог",
         "goods": goods,
   
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    
    product = Products.objects.get(slug=product_slug) # отображаем продукт по слагу
    
    context: dict = {"product": product}
    
    return render(request, "goods/product.html", context=context)
