# Generated by Django 5.0.1 on 2024-01-09 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_alter_stock_stockstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='stockstatus',
            field=models.CharField(max_length=5),
        ),
    ]