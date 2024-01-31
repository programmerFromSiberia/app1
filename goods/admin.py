from django.contrib import admin

from goods.models import Categories, Products

# admin.site.register(Categories)
# admin.site.register(Products)

@admin.register(Categories)  # регистрируем класс в адимнистраторе
class CategoriesAdmin(admin.ModelAdmin):
    #  производим тонкую настройку полей таблиц в адинпанели
    prepopulated_fields = {'slug': ('name',)}  # делаем заполнение поля URL в таблице Категории автоматически

@admin.register(Products)  # регистрируем класс в адимнистраторе
class ProductsAdmin(admin.ModelAdmin):
    #  производим тонкую настройку полей таблиц в адинпанели
    prepopulated_fields = {'slug': ('name',)}  # делаем заполнение поля URL в таблице Продукты автоматически


