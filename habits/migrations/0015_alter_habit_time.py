# Generated by Django 5.0.6 on 2024-11-26 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0014_habit_is_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='time',
            field=models.CharField(blank=True, default='12:00:00', null=True, verbose_name='время когда необходимо выполнять'),
        ),
    ]
