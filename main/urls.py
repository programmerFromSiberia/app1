from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'), # путь к главной странице
    path('about/', views.about, name='about'), # путь к  странице about    
]