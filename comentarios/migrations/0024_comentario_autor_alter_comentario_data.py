# Generated by Django 4.0.4 on 2022-05-09 12:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0023_alter_comentario_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='autor',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comentario',
            name='data',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 9, 9, 28, 53, 559299)),
        ),
    ]
