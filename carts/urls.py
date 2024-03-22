from django.urls import path

from carts import views  #  импортируется из файла carts

app_name = "carts"  # пространство имен

# https://docs.djangoproject.com/en/5.0/topics/http/urls/ - пример конфигурации

urlpatterns = [
    path('cart_add/<slug:product_slug>/', views.cart_add, name='cart_add'), # добавляем товар в корзину
    path('cart_change/<slug:product_slug>/', views.cart_change, name='cart_change'), # изменяем кол-во товара в корзине
    path('cart_remove/<slug:product_slug>/', views.cart_remove, name='cart_remove'), # удаляем товар из корзины
]
