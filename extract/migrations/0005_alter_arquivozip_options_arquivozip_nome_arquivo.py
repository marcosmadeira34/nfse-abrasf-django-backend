# Generated by Django 5.1.7 on 2025-07-03 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extract', '0004_creditpackage_paymentorder_credittransaction_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='arquivozip',
            options={'verbose_name': 'Arquivo ZIP', 'verbose_name_plural': 'Arquivos ZIP'},
        ),
        migrations.AddField(
            model_name='arquivozip',
            name='nome_arquivo',
            field=models.CharField(blank=True, help_text='Nome do arquivo ZIP', max_length=255, null=True),
        ),
    ]
