from django.db import models
from django.conf import settings


class Category(models.Model):
	name = models.CharField(max_length=15,
							blank=False, 
							null=False, 
							verbose_name='Категорія техніки')

	class Meta:
		verbose_name = 'Категорія техніки'
		verbose_name_plural = 'Категорії техніки'

	def __str__(self):
		return self.name # Наприклад - Ноутбук, Планшет, ПК, Радіостанція, Серверна шафа і т.д.


class Equipment(models.Model):
	categoryId = models.ForeignKey(Category,
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

	class Meta:
		verbose_name = 'Техніка'
		verbose_name_plural = 'Техніка'

	def __str__(self):
		return '{} {} S/N:{}'.format(self.categoryId.name, self.name, self.serialNumber)