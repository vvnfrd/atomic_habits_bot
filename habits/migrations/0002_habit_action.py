# Generated by Django 5.0.6 on 2024-11-26 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='action',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='действие'),
        ),
    ]
