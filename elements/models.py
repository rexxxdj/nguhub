from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=15,
							blank=False, 
							null=False, 
							verbose_name='Категорія')

	class Meta:
		verbose_name = 'Категорія складових'
		verbose_name_plural = 'Категорії складових'

	def __str__(self):
		return self.name


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
	serialNumber = models.CharField(max_length=20,
							blank=True, 
							null=True, 
							default = u'Н/Д',
							verbose_name='Серійний номер')
	photo = models.ImageField(upload_to='media/element/%Y/%m/%d', 
							blank=True,
							verbose_name='Фотографія')

	class Meta:
		verbose_name = 'Техніка'
		verbose_name_plural = 'Техніка'

	def __str__(self):
		return '{} {} S/N:{}'.format(self.categoryId.name, self.name, self.serialNumber)