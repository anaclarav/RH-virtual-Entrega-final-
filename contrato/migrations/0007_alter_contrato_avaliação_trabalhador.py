# Generated by Django 4.0.3 on 2022-06-04 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0006_remove_contrato_avaliação_empregador_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='Avaliação_trabalhador',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], max_length=50, null=True),
        ),
    ]
