from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """Модель пользователя"""

    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    telegram_id = models.CharField(unique=True, verbose_name='telegram id', **NULLABLE)
    chat_id = models.CharField(unique=True, verbose_name='telegram id', **NULLABLE)
    first_name = models.CharField(max_length=35, verbose_name='имя', **NULLABLE)
    last_name = models.CharField(max_length=35, verbose_name='имя', **NULLABLE)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'