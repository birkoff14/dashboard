# Generated by Django 3.2 on 2022-03-03 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportInfra', '0016_cierrefalla_idfalla'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cierrefalla',
            old_name='idFAlla',
            new_name='idFalla',
        ),
    ]