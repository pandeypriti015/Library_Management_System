# Generated by Django 2.2.6 on 2019-10-14 10:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0011_auto_20191014_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_of_return',
            field=models.DateField(verbose_name=datetime.datetime(2019, 10, 21, 10, 38, 4, 163295)),
        ),
    ]