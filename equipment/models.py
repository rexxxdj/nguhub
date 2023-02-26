from django.db import models
from django.urls import reverse
from django.conf import settings
from employees.models import Employee


class Category(models.Model):
	name = models.CharField(max_length=50,
							blank=False, 
							null=False, 
							verbose_name='Категорія обладнання')

	class Meta:
		verbose_name = 'Категорія обладнання'
		verbose_name_plural = 'Категорії обладнання'

	def __str__(self):
		return self.name # Наприклад - Ноутбук, Планшет, ПК, Радіостанція, Серверна шафа і т.д.


class Status(models.Model):
	name = models.CharField(max_length=50,
							blank=False,
							null=False,
							verbose_name='Статус обладнання')

	class Meta:
		verbose_name = 'Статус обладнання'
		verbose_name_plural = 'Статуси обладнання'

	def __str__(self):
		return self.name # Наприклад - Знищена, В роботі, На зберіганні, Не обліковано і т.д.


class Equipment(models.Model):
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
	photo = models.ImageField(upload_to='media/equipment/%Y/%m/%d', 
							blank=True,
							verbose_name='Фотографія')
	status = models.ForeignKey(Status,
							on_delete=models.PROTECT,
							blank=True, 
							null=True,
							verbose_name='Статус')
	employee = models.ForeignKey(Employee,
							on_delete=models.PROTECT,
							blank=True, 
							null=True,
							verbose_name='Відповідальний')

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