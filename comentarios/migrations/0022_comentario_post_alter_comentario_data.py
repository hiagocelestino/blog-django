# Generated by Django 4.0.4 on 2022-05-09 07:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_data'),
        ('comentarios', '0021_alter_comentario_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='posts.post'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='data',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 9, 4, 55, 30, 427082)),
        ),
    ]
