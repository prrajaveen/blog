# Generated by Django 4.2.5 on 2023-10-08 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllStocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=500)),
                ('company_name', models.CharField(max_length=500)),
                ('market_cap', models.FloatField()),
            ],
        ),
    ]