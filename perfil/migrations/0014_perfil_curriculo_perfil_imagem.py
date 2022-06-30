# Generated by Django 4.0.3 on 2022-06-23 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0013_perfil_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='curriculo',
            field=models.FileField(blank=True, null=True, upload_to='curriculos/'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='imagem',
            field=models.ImageField(null=True, upload_to='static/imagens_perfil/'),
        ),
    ]
