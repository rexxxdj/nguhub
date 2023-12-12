import datetime
from django.db import models
from django.urls import reverse
from django.conf import settings
from simple_history.models import HistoricalRecords
from employee.models import Employee
from nguhub.models import Location, Placement


class Category(models.Model):
	name = models.CharField(max_length=50,
							blank=False, 
							null=False, 
							verbose_name='Категорія майна')
	notes = models.CharField(max_length=200,
							blank=True, 
							null=True, 
							verbose_name='Додатковий коментар')
	history = HistoricalRecords()

	class Meta:
		verbose_name = 'Категорія майна'
		verbose_name_plural = 'Категорії майна'

	def get_update_url(self):
		return reverse('directory_equipmentcategory_update',
			args=[self.id])

	def get_delete_url(self):
		return reverse('directory_equipmentcategory_delete',
			args=[self.id])

	def __str__(self):
		return self.name # Наприклад - Ноутбук, Планшет, ПК, Радіостанція, Серверна шафа і т.д.


class Status(models.Model):
	name = models.CharField(max_length=50,
							blank=False,
							null=False,
							verbose_name='Статус майна')
	notes = models.CharField(max_length=200,
							blank=True, 
							null=True, 
							verbose_name='Додатковий коментар')
	history = HistoricalRecords()

	class Meta:
		verbose_name = 'Статус майна'
		verbose_name_plural = 'Статуси майна'

	def get_update_url(self):
		return reverse('directory_equipmentstatus_update',
			args=[self.id])

	def get_delete_url(self):
		return reverse('directory_equipmentstatus_delete',
			args=[self.id])

	def __str__(self):
		return self.name # Наприклад - Знищена, В роботі, На зберіганні, Не обліковано і т.д.


class Equipment(models.Model):
	
	UNIT_CHOICES = (
		(1, u'шт.'),
		(2, u'л.'),
		(3, u'кг.'),
		(4, u'у.о.'),
		(5, u'м.кв.'),
		(6, u'м.куб.'),
		(7, u'м.пог.')
    )

	category = models.ForeignKey(Category,
			on_delete=models.PROTECT,
			blank=True, 
			null=True,
			verbose_name='Категорія')
	status = models.ForeignKey(Status,
			on_delete=models.PROTECT,
			blank=True, 
			null=True,
			verbose_name='Статус')
	inventory_name = models.CharField(max_length=2048,
			blank=False, 
			null=False,
			verbose_name='Номенклатурна назва')
	inventory_number = models.CharField(max_length=50,
			blank=True, 
			null=True,
			verbose_name='Інвентарний номер')
	serial_number = models.CharField(max_length=50,
			blank=True, 
			null=True, 
			verbose_name='Серійний номер')
	count = models.DecimalField(max_digits=19, 
			decimal_places=2,
			blank=True, 
			null=True,
			verbose_name='Кількість')
	unit = models.IntegerField(choices=UNIT_CHOICES, 
			blank=False, 
			null=False, 
			default=1,
			verbose_name='Одиниця виміру')
	cost = models.DecimalField(max_digits=19, 
			decimal_places=2,
			blank=True, 
			null=True,
			verbose_name='Первісна вартість за одиницю')
	counterparty = models.ForeignKey(Employee,
			on_delete=models.PROTECT,
			blank=True, 
			null=True,
			related_name='equipment_counterparty',
			verbose_name='Контрагент')
	counterparty_date = models.DateField(default=datetime.date.today,
			blank=True, 
			null=True,
			verbose_name='Дата закріплення за контрагентом')
	counterparty_document = models.CharField(max_length=1024,
			blank=True, 
			null=True,
			verbose_name='Підстава закріплення контрагента')
	ledger_book_number = models.IntegerField(blank=True, 
			null=True,
			verbose_name='Номер книги з записом')
	ledger_book_page  = models.IntegerField(blank=True, 
			null=True,
			verbose_name='Сторінка книги з записом')
	formular_number  = models.IntegerField(blank=True, 
			null=True,
			verbose_name='Номер формуляра')
	complete_set = models.CharField(max_length=4000,
							blank=True, 
							null=True, 
							verbose_name='Комплектація')
	notes = models.CharField(max_length=2048,
							blank=True, 
							null=True, 
							verbose_name='Додатковий коментар')
	history = HistoricalRecords() #istoria


class EquipmentDetail(models.Model):
	RECEIPT_TYPE_CHOICES = (
		(1, u'Закупка'),
		(2, u'Благодійність'),
		(3, u'Переміщення')
		)

	RADIO_TYPE_CHOICES = (
		(1, u'Ретранслятор'),
		(2, u'Автомобільна'),
		(3, u'Портативна'),
		(4, u'Стаціонарна')
		)

	RADIO_FREQUENCY_CHOICES = (
		(1, u'VLF'),
		(2, u'LF'),
		(3, u'MF'),
		(4, u'HF'),
		(5, u'VHF'),
		(6, u'UHF'),
		(7, u'SHF'),
		(8, u'EHF'),
		(9, u'RF'),
		(10, u'-')
		)

	equipment = models.ForeignKey(Equipment,
			on_delete=models.PROTECT,
			blank=False, 
			null=False,
			verbose_name='Обладнання')
	internal_name = models.CharField(max_length=255,
			blank=False, 
			null=False,
			verbose_name='Внутрішня назва')
	internal_number = models.CharField(max_length=50,
			blank=True, 
			null=True, 
			verbose_name='Внутрішній номер')
	receipt_type = models.IntegerField(choices=RECEIPT_TYPE_CHOICES, 
			blank=False, 
			null=False, 
			default=1,
			verbose_name='Тип надходження')
	receipt = models.CharField(max_length=1024,
			blank=True, 
			null=True, 
			verbose_name='Від кого надійшло')
	receipt_date = models.DateField(default=datetime.date.today,
			blank=True, 
			null=True,
			verbose_name='Дата надходження')
	receipt_document = models.CharField(max_length=1024,
			blank=True, 
			null=True,
			verbose_name='Прихідний документ')
	manufacture_date = models.CharField(max_length=50,
			blank=True, 
			null=True, 
			verbose_name='Дата виготовлення')
	service_life = models.CharField(max_length=50,
			blank=True, 
			null=True, 
			verbose_name='Термін експлуатації')
	warranty_period = models.CharField(max_length=50,
			blank=True, 
			null=True, 
			verbose_name='Гарантійний строк')
	operation_date = models.DateField(default=datetime.date.today,
			blank=True, 
			null=True,
			verbose_name='Дата введення в експлуатацію')
	operation_document = models.CharField(max_length=1024,
			blank=True, 
			null=True,
			verbose_name='Документ введення в експлуатацію')
	direction = models.ForeignKey(Employee,
			on_delete=models.PROTECT,
			blank=True, 
			null=True,
			related_name='equipment_direction',
			verbose_name='Відповідальний за напрямком')
	location = models.ForeignKey(Placement,
			on_delete=models.PROTECT,
			blank=True,
			null=True,
			verbose_name='Місцезнаходження')
	employee = models.ForeignKey(Employee,
			on_delete=models.PROTECT,
			blank=True, 
			null=True,
			related_name='equipment_employee',
			verbose_name='Користувач')
	employee_date = models.DateField(default=datetime.date.today,
			blank=True, 
			null=True,
			verbose_name='Дата закріплення за користувачем')
	counterparty_document = models.CharField(max_length=1024,
			blank=True, 
			null=True,
			verbose_name='Підстава закріплення користувача')
	radio_type = models.IntegerField(choices=RADIO_TYPE_CHOICES, 
			blank=False, 
			null=False, 
			default=1,
			verbose_name='Тип радіовиробу')
	radio_frequency_type  = models.IntegerField(choices=RADIO_FREQUENCY_CHOICES, 
			blank=False, 
			null=False, 
			default=6,
			verbose_name='Діапазон радіовиробу')
	radio_model = models.CharField(max_length=1024,
			blank=True, 
			null=True,
			verbose_name='Модель радіовиробу')
	firmware_version = models.CharField(max_length=1024,
			blank=True, 
			null=True,
			verbose_name='Версія мікромпрограми')
	codeplug_name = models.CharField(max_length=1024,
			blank=True, 
			null=True,
			verbose_name='Назва зашитого файла шифрування')
	codeplug_last_date = models.DateField(default=datetime.date.today,
			blank=True, 
			null=True,
			verbose_name='Остання дата прошивки')
	motorola_audit = models.CharField(max_length=1024,
			blank=True, 
			null=True,
			verbose_name='Перевірка по базі Mototrola')
	notes = models.CharField(max_length=2048,
							blank=True, 
							null=True, 
							verbose_name='Додатковий коментар')
	history = HistoricalRecords() #istoria

	def equipment__name(self, instance):
		return instance.equipment.name

	def equipment__serial_number(self, instance):
		return instance.equipment.serial_number

	def get_update_url(self):
		return reverse('equipment_detail:update',
			args=[self.id])

	def get_delete_url(self):
		return reverse('equipment_detail:delete',
			args=[self.id])

	class Meta:
		verbose_name = 'Відомості про обладнання'
		verbose_name_plural = 'Відомості про обладнання'

	def __str__(self):
		return '{} S/N:{}'.format(self.name, self.serialNumber)