# Generated by Django 5.0.6 on 2024-11-26 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0006_alter_habit_time_to_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='time_to_complete',
            field=models.TimeField(blank=True, default='0:01:30', null=True, verbose_name='время на выполнение'),
        ),
    ]
