# Generated by Django 4.0.3 on 2022-06-01 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0008_alter_perfil_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='categoria',
        ),
    ]
