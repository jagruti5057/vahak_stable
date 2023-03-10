# Generated by Django 4.1.3 on 2023-01-12 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0029_attachnewlorry_expired_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postload',
            name='is_completed',
        ),
        migrations.RemoveField(
            model_name='postload',
            name='is_expired',
        ),
        migrations.RemoveField(
            model_name='postload',
            name='is_in_active',
        ),
        migrations.RemoveField(
            model_name='postload',
            name='is_in_progress',
        ),
        migrations.RemoveField(
            model_name='postload',
            name='is_in_transit',
        ),
        migrations.AddField(
            model_name='postload',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('in_progress', 'in_progress'), ('in_transit', 'in_transit'), ('completed', 'completed'), ('expired', 'expired')], default='active', max_length=20),
        ),
    ]
