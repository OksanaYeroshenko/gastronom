# Generated by Django 2.2 on 2020-11-10 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
	('notifications', '0001_initial'),
    ]

    operations = [
        
        migrations.AlterField(
            model_name='notification',
            name='send_method',
            field=models.CharField(choices=[('email', 'E-mail'), ('messenger', 'Messenger'), ('site', 'Site')], default='email', max_length=20),
        ),
    ]
