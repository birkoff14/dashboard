# Generated by Django 3.2 on 2022-07-18 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportinfra', '0008_auto_20220706_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividades',
            name='Solicitante',
            field=models.CharField(blank=True, max_length=100, verbose_name='Solicitante'),
        ),
    ]