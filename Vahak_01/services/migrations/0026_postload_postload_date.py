# Generated by Django 4.1.3 on 2023-01-11 05:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0025_remove_postload_routes_attachnewlorry_routes'),
    ]

    operations = [
        migrations.AddField(
            model_name='postload',
            name='postload_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
