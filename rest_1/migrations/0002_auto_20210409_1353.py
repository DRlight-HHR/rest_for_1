# Generated by Django 3.2 on 2021-04-09 09:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='temp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('password', models.CharField(max_length=150)),
                ('temp', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 4, 9, 13, 53, 59, 199137)),
        ),
    ]
