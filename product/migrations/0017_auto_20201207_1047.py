# Generated by Django 2.2 on 2020-12-07 08:47

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_auto_20201126_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmedia',
            name='product_image',
            field=models.ImageField(null=True, upload_to='products/%Y/%m/%d/original/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
