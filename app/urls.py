"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Представления функций
    1. Добавьте импорт: из представлений импорта my_app.
    2. Добавьте URL-адрес в urlpatterns: path('',views.home, name='home')
Представления на основе классов
    1. Добавляем импорт: fromother_app.views import Home
    2. Добавьте URL-адрес в urlpatterns: path('', Home.as_view(), name='home')
Включение другого URLconf
    1. Импортируйте функцию include(): из django.urls import include, путь
    2. Добавьте URL-адрес в urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from app import settings


urlpatterns = [
    path('admin/', admin.site.urls), # путь к админ панели
    path('', include('main.urls', namespace='main')), # путь к главной странице
    path('catalog/', include('goods.urls', namespace='catalog')), # путь к странице каталога
    
]

if settings.DEBUG:
    urlpatterns += [
       path("__debug__/", include("debug_toolbar.urls")),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
    
    
    
    
