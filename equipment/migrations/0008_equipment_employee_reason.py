# Generated by Django 4.1.6 on 2023-02-27 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0007_alter_equipment_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='employee_reason',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Підстава закріплення користувача'),
        ),
    ]
