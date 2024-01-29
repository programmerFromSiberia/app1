from django.urls import path

from goods import views  #  импортируется из файла goods

app_name = 'goods'

urlpatterns = [
    path('', views.catalog, name='index'), # путь к каталогу товаров
    path('product/', views.product, name='product'), # путь к  продуктам    
]