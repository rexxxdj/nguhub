# Generated by Django 4.1.6 on 2023-03-22 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departmentEquipment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='operationDate_reason',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Підстава введення в експлуатацію'),
        ),
        migrations.AddField(
            model_name='historicalequipment',
            name='operationDate_reason',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Підстава введення в експлуатацію'),
        ),
    ]
