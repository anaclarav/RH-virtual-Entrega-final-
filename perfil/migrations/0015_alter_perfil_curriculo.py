# Generated by Django 4.0.3 on 2022-06-27 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0014_perfil_curriculo_perfil_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='curriculo',
            field=models.FileField(blank=True, null=True, upload_to='static/curriculos/'),
        ),
    ]