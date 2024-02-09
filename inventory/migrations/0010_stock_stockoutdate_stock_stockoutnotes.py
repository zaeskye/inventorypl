# Generated by Django 5.0.1 on 2024-01-11 01:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_alter_suppliers_supplier_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='stockoutdate',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='stock',
            name='stockoutnotes',
            field=models.TextField(default=''),
        ),
    ]
