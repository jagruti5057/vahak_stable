# Generated by Django 4.1.3 on 2022-12-29 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_rename_phone_user_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phonenumber',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
