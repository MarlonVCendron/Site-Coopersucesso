# Generated by Django 3.0.3 on 2020-08-11 12:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20200804_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='cod1_produto',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='produto',
            name='cod2_produto',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='produto',
            name='info1_produto',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='produto',
            name='info2_produto',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 11, 9, 2, 20, 288261), verbose_name='Data publicação'),
        ),
    ]
