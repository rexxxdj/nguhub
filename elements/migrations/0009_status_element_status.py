# Generated by Django 4.1.6 on 2023-02-19 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elements', '0008_alter_element_serialnumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Статус комплектуючих')),
            ],
            options={
                'verbose_name': 'Статус комплектуючих',
                'verbose_name_plural': 'Статуси комплектуючих',
            },
        ),
        migrations.AddField(
            model_name='element',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='elements.status', verbose_name='Статус'),
        ),
    ]
