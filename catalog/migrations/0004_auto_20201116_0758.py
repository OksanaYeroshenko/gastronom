# Generated by Django 2.2 on 2020-11-16 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20201116_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='index',
            field=models.IntegerField(default=0),
        ),
    ]
