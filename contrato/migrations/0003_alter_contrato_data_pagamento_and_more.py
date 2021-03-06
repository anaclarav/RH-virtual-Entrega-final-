# Generated by Django 4.0.3 on 2022-05-27 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0002_alter_contrato_detalhes_contrato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='data_pagamento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='data_serviço',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='status_contrato',
            field=models.CharField(choices=[('1', 'Em aberto'), ('2', 'Finalizado'), ('3', 'Cancelado')], default='1', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='status_pagamento',
            field=models.CharField(choices=[('1', 'Aguardando'), ('2', 'Realizado')], default='1', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='status_serviço',
            field=models.CharField(choices=[('1', 'Agendado'), ('2', 'Em andamento'), ('3', 'Realizado')], default='1', max_length=50, null=True),
        ),
    ]
