# Generated by Django 4.1.3 on 2022-12-26 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_rename_is_bank_varified_user_is_bank_verified_and_more'),
        ('services', '0008_attachnewlorry_routes_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachnewlorry',
            name='routes_name',
        ),
        migrations.AddField(
            model_name='postload',
            name='routes_name',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='account.routes'),
        ),
    ]
