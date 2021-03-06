# Generated by Django 3.0.3 on 2020-08-11 12:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20200811_0902'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='cod1_produto',
            new_name='cod1',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='cod2_produto',
            new_name='cod2',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='cod3_produto',
            new_name='cod3',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='desc_produto',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='imagem_produto',
            new_name='imagem',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='info1_produto',
            new_name='info1',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='info2_produto',
            new_name='info2',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='info3_produto',
            new_name='info3',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='nome_produto',
            new_name='nome',
        ),
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 11, 9, 24, 59, 158202), verbose_name='Data publicação'),
        ),
    ]
