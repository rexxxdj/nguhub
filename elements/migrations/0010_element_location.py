# Generated by Django 4.1.6 on 2023-02-27 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nguhub', '0001_initial'),
        ('elements', '0009_status_element_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='nguhub.location', verbose_name='Місце закріплення'),
        ),
    ]