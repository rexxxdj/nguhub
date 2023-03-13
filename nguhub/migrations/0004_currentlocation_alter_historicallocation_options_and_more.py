# Generated by Django 4.1.6 on 2023-03-12 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nguhub', '0003_historicallocation_delete_reason_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Місце знаходження')),
                ('delete_reason', models.CharField(blank=True, max_length=50, null=True, verbose_name='Причина видалення')),
            ],
            options={
                'verbose_name': 'Поточне місцезнаходження',
                'verbose_name_plural': 'Поточне місцезнаходження',
            },
        ),
        migrations.AlterModelOptions(
            name='historicallocation',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Місце закріплення', 'verbose_name_plural': 'historical Місце закріплення'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'Місце закріплення', 'verbose_name_plural': 'Місце закріплення'},
        ),
        migrations.AlterField(
            model_name='historicallocation',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Місце закріплення'),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Місце закріплення'),
        ),
        migrations.CreateModel(
            name='HistoricalCurrentLocation',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Місце знаходження')),
                ('delete_reason', models.CharField(blank=True, max_length=50, null=True, verbose_name='Причина видалення')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Поточне місцезнаходження',
                'verbose_name_plural': 'historical Поточне місцезнаходження',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]