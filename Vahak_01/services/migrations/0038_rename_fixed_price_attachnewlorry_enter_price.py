# Generated by Django 4.1.3 on 2023-01-19 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0037_attachnewlorry_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attachnewlorry',
            old_name='fixed_price',
            new_name='enter_price',
        ),
    ]
