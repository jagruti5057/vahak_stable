# Generated by Django 4.1.3 on 2022-12-29 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0024_remove_user_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
