# Generated by Django 4.1.3 on 2022-12-29 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0025_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(max_length=30),
        ),
    ]