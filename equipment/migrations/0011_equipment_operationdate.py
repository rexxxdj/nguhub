# Generated by Django 4.1.6 on 2023-02-27 15:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0010_equipment_fixed_equipment_fixed_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='operationDate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
