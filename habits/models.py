import datetime
from django.db import models
from config import settings

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='telegram id')
    place = models.CharField(max_length=100, verbose_name='место привычки', **NULLABLE)
    time = models.TimeField(default=datetime.time(hour=12), verbose_name='время когда необходимо выполнять', **NULLABLE)
    action = models.CharField(max_length=100, verbose_name='действие', **NULLABLE)
    useful_bonus = models.CharField(max_length=35, verbose_name='признак полезной привычки', **NULLABLE)
    associated_habit = models.ForeignKey("Habit", on_delete=models.CASCADE, verbose_name='связанная привычка', **NULLABLE)
    periodicity = models.IntegerField(default=datetime.timedelta(days=1), verbose_name='перодичность в днях')
    reward = models.CharField(max_length=100, verbose_name='вознаграждение', **NULLABLE)
    time_to_complete = models.TimeField(default=datetime.timedelta(minutes=1, seconds=30), verbose_name='время на выполнение')



    def __str__(self):
        return f'{self.user} {self.action}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'