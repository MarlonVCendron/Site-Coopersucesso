# Generated by Django 3.0.3 on 2020-07-14 17:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200714_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 14, 30, 41, 292331), verbose_name='Data publicação'),
        ),
    ]
