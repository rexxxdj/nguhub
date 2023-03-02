import datetime
from django.urls import reverse
from simple_history.models import HistoricalRecords
from django.db import models
from equipment.models import Equipment
from employees.models import Employee
from nguhub.models import Location


class Category(models.Model):
	name = models.CharField(max_length=35,
							blank=False, 
							null=False, 
							verbose_name='Категорія')
	history = HistoricalRecords()

	class Meta:
		verbose_name = 'Категорія'
		verbose_name_plural = 'Категорії'

	def __str__(self):
		return self.name

class Status(models.Model):
	name = models.CharField(max_length=50,
							blank=False,
							null=False,
							verbose_name='Статус комплектуючих')
	history = HistoricalRecords()

	class Meta:
		verbose_name = 'Статус комплектуючих'
		verbose_name_plural = 'Статуси комплектуючих'

	def __str__(self):
		return self.name # Наприклад - Знищена, В роботі, На зберіганні, Не обліковано і т.д.


class Element(models.Model):
	category = models.ForeignKey(Category,
							on_delete=models.PROTECT,
							default = 0,
							verbose_name='Категорія')
	name = models.CharField(max_length=1024,
							blank=False, 
							null=False,
							default = u'Н/Д',
							verbose_name='Назва')
	value = models.CharField(max_length=20,
							blank=False, 
							null=False,
							default = u'1 шт.',
							verbose_name='Кількість')
	serialNumber = models.CharField(max_length=20,
							blank=True, 
							null=True,
							verbose_name='Серійний номер')
	photo = models.ImageField(upload_to='media/element/%Y/%m/%d', 
							blank=True,
							verbose_name='Фотографія')
	equipment = models.ForeignKey(Equipment,
							on_delete=models.SET_NULL,
							blank=True,
							null = True,
							verbose_name='Встановлено на обладнання',
							related_name='elements')
	operationDate = models.DateField(default=datetime.date.today,
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
							related_name='element_responsible',
							verbose_name='Матеріально Відповідальний')
	responsible_reason = models.CharField(max_length=100,
							blank=True, 
							null=True,
							verbose_name='Підстава закріплення матеріально відповідального')
	fixed = models.ForeignKey(Employee,
							on_delete=models.PROTECT,
							blank=True, 
							null=True,
							related_name='element_fixed',
							verbose_name='За ким закріплено')
	fixed_reason = models.CharField(max_length=100,
							blank=True, 
							null=True,
							verbose_name='Підстава закріплення відповідального')
	employee = models.ForeignKey(Employee,
							on_delete=models.PROTECT,
							blank=True, 
							null=True,
							related_name='element_employee',
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

	class Meta:
		verbose_name = 'Комплектуючі'
		verbose_name_plural = 'Комплектуючі'

	def get_absolute_url(self):
		return reverse('element:detail',
			args=[self.id])

	def get_update_url(self):
		return reverse('element:update',
			args=[self.id])

	def get_delete_url(self):
		return reverse('element:delete',
			args=[self.id])

	def __str__(self):
		return '{} {} S/N:{}'.format(self.category.name, self.name, self.serialNumber)