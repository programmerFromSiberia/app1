from django.urls import path

from users import views

app_name = "users"

urlpatterns = [
    path("login/", views.login, name="login"),  # путь к главной странице
    path("registration/", views.registration, name="registration"),  # путь к  странице регистрации registration
    path("profile/", views.profile, name="profile"), # путь к странице профиля
    path("logout/", views.logout, name="logout"), # путь к странице выхода
]
