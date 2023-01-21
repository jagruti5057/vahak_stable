# Generated by Django 4.1.3 on 2023-01-04 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0017_postload_completed_postload_in_transit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postload',
            old_name='active',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='postload',
            old_name='completed',
            new_name='is_completed',
        ),
        migrations.RenameField(
            model_name='postload',
            old_name='expired',
            new_name='is_expired',
        ),
        migrations.RenameField(
            model_name='postload',
            old_name='in_progress',
            new_name='is_in_progress',
        ),
        migrations.RenameField(
            model_name='postload',
            old_name='in_transit',
            new_name='is_in_transit',
        ),
    ]
