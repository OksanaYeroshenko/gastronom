# Generated by Django 2.2 on 2020-12-14 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0003_merge_20201213_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountcart',
            name='valid_date_start',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Active from'),
        ),
    ]