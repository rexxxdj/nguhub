# Generated by Django 4.1.6 on 2023-02-16 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0003_status_alter_category_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipment',
            old_name='categoryId',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='equipment',
            old_name='statusId',
            new_name='status',
        ),
    ]
