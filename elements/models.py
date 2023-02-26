from django.urls import reverse
from django.db import models
from equipment.models import Equipment


class Category(models.Model):
	name = models.CharField(max_length=35,
							blank=False, 
							null=False, 
							verbose_name='Категорія')

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
	status = models.ForeignKey(Status,
							on_delete=models.PROTECT,
							blank=True, 
							null=True,
							verbose_name='Статус')

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