# Generated by Django 4.1.6 on 2023-02-27 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_employee_photo_alter_employee_rank'),
        ('elements', '0011_alter_element_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='element_employee', to='employees.employee', verbose_name='Користувач'),
        ),
        migrations.AddField(
            model_name='element',
            name='employee_reason',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Підстава закріплення користувача'),
        ),
        migrations.AddField(
            model_name='element',
            name='fixed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='element_fixed', to='employees.employee', verbose_name='За ким закріплено'),
        ),
        migrations.AddField(
            model_name='element',
            name='fixed_reason',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Підстава закріплення відповідального'),
        ),
        migrations.AddField(
            model_name='element',
            name='responsible',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='element_responsible', to='employees.employee', verbose_name='Матеріально Відповідальний'),
        ),
        migrations.AddField(
            model_name='element',
            name='responsible_reason',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Підстава закріплення матеріально відповідального'),
        ),
    ]
