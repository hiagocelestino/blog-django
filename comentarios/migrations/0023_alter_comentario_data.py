# Generated by Django 4.0.4 on 2022-05-09 08:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0022_comentario_post_alter_comentario_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='data',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 9, 5, 6, 34, 208205)),
        ),
    ]
