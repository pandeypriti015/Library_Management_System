# Generated by Django 2.2.6 on 2019-10-12 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]