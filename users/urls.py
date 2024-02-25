from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'), # путь к странице авторизации
    path('registration/', views.registration, name='registration'),  # путь к  странице регистрации registration
    path('users-cart/', views.users_cart, name='users_cart'), # путь к странице корзины
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'), # путь к странице выхода из профиля
]
