# Generated by Django 4.1.6 on 2023-03-12 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0019_alter_equipment_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='delete_reason',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Причина видалення'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='delete_reason',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Причина видалення'),
        ),
        migrations.AddField(
            model_name='historicalcategory',
            name='delete_reason',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Причина видалення'),
        ),
        migrations.AddField(
            model_name='historicalequipment',
            name='delete_reason',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Причина видалення'),
        ),
        migrations.AddField(
            model_name='historicalstatus',
            name='delete_reason',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Причина видалення'),
        ),
        migrations.AddField(
            model_name='status',
            name='delete_reason',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Причина видалення'),
        ),
    ]
