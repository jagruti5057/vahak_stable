# Generated by Django 4.1.3 on 2023-01-05 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0028_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
