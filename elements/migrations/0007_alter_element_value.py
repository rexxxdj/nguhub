# Generated by Django 4.1.6 on 2023-02-19 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elements', '0006_element_value_alter_element_equipment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='value',
            field=models.CharField(default='1 шт.', max_length=20, verbose_name='Кількість'),
        ),
    ]
