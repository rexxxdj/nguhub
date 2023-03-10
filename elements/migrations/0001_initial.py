# Generated by Django 4.1.6 on 2023-02-15 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Категорія')),
            ],
            options={
                'verbose_name': 'Категорія складових',
                'verbose_name_plural': 'Категорії складових',
            },
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Н/Д', max_length=1024, verbose_name='Назва')),
                ('serialNumber', models.CharField(blank=True, default='Н/Д', max_length=20, null=True, verbose_name='Серійний номер')),
                ('photo', models.ImageField(blank=True, upload_to='media/element/%Y/%m/%d', verbose_name='Фотографія')),
                ('categoryId', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='elements.category', verbose_name='Категорія')),
            ],
            options={
                'verbose_name': 'Техніка',
                'verbose_name_plural': 'Техніка',
            },
        ),
    ]
