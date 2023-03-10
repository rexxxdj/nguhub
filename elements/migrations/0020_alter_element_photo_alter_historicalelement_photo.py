# Generated by Django 4.1.6 on 2023-03-09 14:58

from django.db import migrations, models
import elements.models


class Migration(migrations.Migration):

    dependencies = [
        ('elements', '0019_element_cost_element_inventorynumber_element_unit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=elements.models.Element.directory_path, verbose_name='Фотографія'),
        ),
        migrations.AlterField(
            model_name='historicalelement',
            name='photo',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Фотографія'),
        ),
    ]
