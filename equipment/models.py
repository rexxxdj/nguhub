import datetime
from django.db import models
from django.urls import reverse
from django.conf import settings
from simple_history.models import HistoricalRecords
from employees.models import Employee
from nguhub.models import Location


class Category(models.Model):
	name = models.CharField(max_length=50,
							blank=False, 
							null=False, 
							verbose_name='Категорія обладнання')
	notes = models.CharField(max_length=200,
							blank=True, 
							null=True, 
							verbose_name='Додаткові коментарі')
	history = HistoricalRecords()

	class Meta:
		verbose_name = 'Категорія обладнання'
		verbose_name_plural = 'Категорії обладнання'

	def get_update_url(self):
		return reverse('directory_equipment_category_update',
			args=[self.id])

	def get_delete_url(self):
		return reverse('directory_equipment_category_delete',
			args=[self.id])

	def __str__(self):
		return self.name # Наприклад - Ноутбук, Планшет, ПК, Радіостанція, Серверна шафа і т.д.


class Status(models.Model):
	name = models.CharField(max_length=50,
							blank=False,
							null=False,
							verbose_name='Статус обладнання')
	notes = models.CharField(max_length=200,
							blank=True, 
							null=True, 
							verbose_name='Додаткові коментарі')
	history = HistoricalRecords()

	class Meta:
		verbose_name = 'Статус обладнання'
		verbose_name_plural = 'Статуси обладнання'

	def get_update_url(self):
		return reverse('directory_equipment_status_update',
			args=[self.id])

	def get_delete_url(self):
		return reverse('directory_equipment_status_delete',
			args=[self.id])

	def __str__(self):
		return self.name # Наприклад - Знищена, В роботі, На зберіганні, Не обліковано і т.д.


class Equipment(models.Model):
	def directory_path(instance, filename):
		return 'media/equipment/{0}/{1}'.format(instance.id, filename)

	category = models.ForeignKey(Category,
							on_delete=models.PROTECT,
							default = 0,
							verbose_name='Категорія')
	name = models.CharField(max_length=1024,
							blank=False, 
							null=False,
							default = u'Н/Д',
							verbose_name='Назва техніки')
	serialNumber = models.CharField(max_length=20,
							blank=True, 
							null=True, 
							default = u'Н/Д',
							verbose_name='Серійний номер')
	photo = models.ImageField(upload_to=directory_path, 
							blank=True,
							verbose_name='Фотографія')
	operationDate = models.DateField(default=datetime.date.today,
							blank=True, 
							null=True,
							verbose_name='Дата введення в експлуатацію')
	status = models.ForeignKey(Status,
							on_delete=models.PROTECT,
							blank=True, 
							null=True,
							verbose_name='Статус')
	location = models.ForeignKey(Location,
							on_delete=models.PROTECT,
							blank=False,
							null=False,
							default=1,
							verbose_name='Місце закріплення')
	responsible = models.ForeignKey(Employee,
							on_delete=models.PROTECT,
							blank=True, 
							null=True,
							related_name='equipment_responsible',
							verbose_name='Матеріально Відповідальний')
	responsible_reason = models.CharField(max_length=100,
							blank=True, 
							null=True,
							verbose_name='Підстава закріплення матеріально відповідального')
	fixed = models.ForeignKey(Employee,
							on_delete=models.PROTECT,
							blank=True, 
							null=True,
							related_name='equipment_fixed',
							verbose_name='За ким закріплено')
	fixed_reason = models.CharField(max_length=100,
							blank=True, 
							null=True,
							verbose_name='Підстава закріплення відповідального')
	employee = models.ForeignKey(Employee,
							on_delete=models.PROTECT,
							blank=True, 
							null=True,
							related_name='equipment_employee',
							verbose_name='Користувач')
	employee_reason = models.CharField(max_length=100,
							blank=True, 
							null=True,
							verbose_name='Підстава закріплення користувача')
	comment = models.CharField(max_length=2048,
							blank=True, 
							null=True, 
							verbose_name='Додатковий коментар')
	history = HistoricalRecords()

	def get_absolute_url(self):
		return reverse('equipment:detail',
			args=[self.id])

	def get_update_url(self):
		return reverse('equipment:update',
			args=[self.id])

	def get_delete_url(self):
		return reverse('equipment:delete',
			args=[self.id])

	class Meta:
		verbose_name = 'Обладнання'
		verbose_name_plural = 'Обладнання'

	def __str__(self):
		return '{} {} S/N:{}'.format(self.category.name, self.name, self.serialNumber)