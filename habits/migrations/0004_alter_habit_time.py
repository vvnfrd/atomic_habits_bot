# Generated by Django 5.0.6 on 2024-11-26 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_alter_habit_periodicity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='time',
            field=models.TimeField(blank=True, default='12:00:00', null=True, verbose_name='время когда необходимо выполнять'),
        ),
    ]
