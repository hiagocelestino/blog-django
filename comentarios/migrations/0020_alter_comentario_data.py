# Generated by Django 4.0.4 on 2022-05-09 06:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0019_alter_comentario_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='data',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 9, 3, 27, 19, 34791)),
        ),
    ]
