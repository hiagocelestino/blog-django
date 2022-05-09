# Generated by Django 4.0.4 on 2022-05-09 04:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('corpo_comentario', models.TextField()),
                ('data', models.DateField(blank=True, default=datetime.datetime(2022, 5, 9, 1, 41, 30, 961653))),
            ],
        ),
    ]