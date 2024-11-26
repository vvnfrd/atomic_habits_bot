# import datetime
from django.db import models
from config import settings

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    """Модель привычки"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    place = models.CharField(max_length=100, verbose_name='место привычки', **NULLABLE)
    time = models.CharField(default="12:00:00", verbose_name='время когда необходимо выполнять', **NULLABLE)
    action = models.CharField(max_length=100, verbose_name='действие')
    pleasantly = models.BooleanField(default=False, verbose_name='признак полезной привычки', **NULLABLE)
    associated_habit = models.ForeignKey("Habit",
                                         on_delete=models.CASCADE, verbose_name='связанная привычка', **NULLABLE)
    periodicity = models.IntegerField(default=1, verbose_name='перодичность в днях')
    reward = models.CharField(max_length=100, verbose_name='вознаграждение', **NULLABLE)
    time_to_complete = models.CharField(default="00:01:30", verbose_name='время на выполнение', **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')

    def __str__(self):
        return f'{self.user} {self.action}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
