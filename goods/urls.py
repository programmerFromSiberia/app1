from django.urls import path

from goods import views  #  импортируется из файла goods

app_name = 'goods'

# https://docs.djangoproject.com/en/5.0/topics/http/urls/ - пример конфигурации

urlpatterns = [
    path('<slug:category_slug>/', views.catalog, name='index'), # путь к каталогу товаров
    path('product/<slug:product_slug>/', views.product, name='product'), # путь к  продуктам прописываем product_id во views   
]