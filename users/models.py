from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): # наследуемся от AbstractUser
    image = models.ImageField(upload_to="users_images", blank=True, null=True, verbose_name='Аватар') # поле для загрузки изображения
    
    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'
        

    def __str__(self):
        return self.username
    