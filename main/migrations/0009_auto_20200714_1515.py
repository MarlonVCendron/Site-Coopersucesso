# Generated by Django 3.0.3 on 2020-07-14 18:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200714_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 15, 15, 42, 392920), verbose_name='Data publicação'),
        ),
        migrations.AlterField(
            model_name='receita',
            name='imagem_preview',
            field=models.ImageField(default='static/default_image.png', upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
