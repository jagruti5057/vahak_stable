# Generated by Django 4.1.3 on 2022-12-30 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0014_postload_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postload',
            old_name='is_active',
            new_name='active',
        ),
    ]
