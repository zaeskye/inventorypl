# Generated by Django 5.0.1 on 2024-01-11 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_stock_stockoutdate_stock_stockoutnotes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('receiverworknum', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('receivername', models.TextField()),
                ('receiverposition', models.TextField()),
            ],
        ),
    ]
