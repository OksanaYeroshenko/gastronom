# Generated by Django 2.2 on 2020-11-28 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0019_auto_20201128_1433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='telegramincomemessage',
            old_name='telegramuser',
            new_name='telegramuser_id',
        ),
    ]
