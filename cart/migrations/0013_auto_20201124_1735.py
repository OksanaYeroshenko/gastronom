# Generated by Django 2.2 on 2020-11-24 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0012_auto_20201123_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, null=True, blank=True, to='product.Product', verbose_name='Product'),
        ),
    ]
