# Generated by Django 4.1.3 on 2023-01-11 06:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0026_postload_postload_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachnewlorry',
            name='updated_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
