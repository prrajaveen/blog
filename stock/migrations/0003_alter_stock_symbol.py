# Generated by Django 4.2.5 on 2023-10-08 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_rename_allstocks_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='symbol',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
