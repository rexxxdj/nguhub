# Generated by Django 4.1.6 on 2023-02-27 15:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elements', '0012_element_employee_element_employee_reason_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='operationDate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
