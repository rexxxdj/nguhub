# Generated by Django 4.1.6 on 2023-02-28 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elements', '0013_element_operationdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='comment',
            field=models.CharField(blank=True, max_length=2048, null=True, verbose_name='Додатковий коментар'),
        ),
        migrations.AlterField(
            model_name='element',
            name='operationDate',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата введення в експлуатацію'),
        ),
    ]