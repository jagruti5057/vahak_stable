# Generated by Django 4.1.3 on 2023-01-20 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0033_helpsupport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helpsupport',
            name='qa_data',
            field=models.TextField(default=None),
        ),
    ]