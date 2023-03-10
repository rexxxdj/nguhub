# Generated by Django 4.1.6 on 2023-02-19 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0005_equipment_employee'),
        ('elements', '0003_element_equipment_alter_category_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категорія', 'verbose_name_plural': 'Категорії'},
        ),
        migrations.AlterModelOptions(
            name='element',
            options={'verbose_name': 'Комплектуючі', 'verbose_name_plural': 'Комплектуючі'},
        ),
        migrations.AlterField(
            model_name='element',
            name='equipment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='equipment.equipment', verbose_name='Встановлено на обладнання'),
        ),
    ]
