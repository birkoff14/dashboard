# Generated by Django 3.2 on 2022-06-22 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportinfra', '0006_auto_20220621_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividades',
            name='Descripcion',
            field=models.CharField(blank=True, max_length=500, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='actividades',
            name='Evento',
            field=models.CharField(blank=True, max_length=150, verbose_name='Evento'),
        ),
    ]