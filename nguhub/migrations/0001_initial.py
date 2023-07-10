# Generated by Django 4.1.6 on 2023-07-01 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Назва')),
                ('address', models.CharField(max_length=1024, verbose_name='Адреса')),
                ('notes', models.CharField(blank=True, max_length=2048, null=True, verbose_name='Примітка')),
            ],
            options={
                'verbose_name': 'Локація розташування',
                'verbose_name_plural': 'Локації розташування',
            },
        ),
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Назва')),
                ('notes', models.CharField(blank=True, max_length=2048, null=True, verbose_name='Примітка')),
                ('location', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='nguhub.location', verbose_name='Локація')),
            ],
            options={
                'verbose_name': 'Місце розташування',
                'verbose_name_plural': 'Місця розташування',
            },
        ),
        migrations.CreateModel(
            name='HistoricalLocation',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Назва')),
                ('address', models.CharField(max_length=1024, verbose_name='Адреса')),
                ('notes', models.CharField(blank=True, max_length=2048, null=True, verbose_name='Примітка')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Локація розташування',
                'verbose_name_plural': 'historical Локації розташування',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
