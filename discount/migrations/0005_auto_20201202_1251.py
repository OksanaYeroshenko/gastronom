# Generated by Django 2.2 on 2020-12-02 10:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0004_auto_20201201_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountcart',
            name='valid_date_end',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 2, 10, 51, 56, 605957, tzinfo=utc), verbose_name='Active to'),
        ),
    ]
