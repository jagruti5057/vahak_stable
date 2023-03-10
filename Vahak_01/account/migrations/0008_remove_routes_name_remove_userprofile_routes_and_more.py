# Generated by Django 4.1.3 on 2022-12-14 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_routes_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routes',
            name='name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='routes',
        ),
        migrations.AddField(
            model_name='routes',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='routes',
            field=models.ManyToManyField(blank=True, default=None, related_name='user_role', to='account.routes'),
        ),
    ]
