# Generated by Django 3.0.3 on 2020-04-22 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_usersession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersession',
            name='ended',
            field=models.BooleanField(default=False),
        ),
    ]