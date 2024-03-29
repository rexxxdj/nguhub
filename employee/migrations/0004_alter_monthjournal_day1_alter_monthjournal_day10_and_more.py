# Generated by Django 4.1.6 on 2023-07-11 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_monthjournal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthjournal',
            name='day1',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day10',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day11',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day12',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day13',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day14',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day15',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day16',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day17',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day18',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day19',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day2',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day20',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day21',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day22',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day23',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day24',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day25',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day26',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day27',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day28',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day29',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day3',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day30',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day31',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day4',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day5',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day6',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day7',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day8',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='day9',
            field=models.CharField(choices=[('Ч', 'Несення бойового чергування (24 години)'), ('Д', 'Несення денного бойового чергування (12 години)'), ('Н', 'Несення нічного бойового чергування (12 години)'), ('З', 'Заняття з бойової та спеціальної підготовки'), ('Р', 'Робочий день (8 годин)'), ('ВХ', 'Вихідний день'), ('Л', 'Лікарняний'), ('ВП', 'Відпустка')], default='Р', max_length=10),
        ),
    ]
