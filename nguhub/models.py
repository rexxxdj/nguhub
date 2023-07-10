from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords


class Location(models.Model):
	name = models.CharField(max_length=50,
							blank=False,
							null=False,
							verbose_name='Назва')
	address = models.CharField(max_length=1024,
							   blank=False,
							   null=False,
							   verbose_name='Адреса')
	notes = models.CharField(max_length=2048,
							blank=True,
							null=True,
							verbose_name='Примітка')
	history = HistoricalRecords()

	class Meta:
		verbose_name = 'Локація розташування'
		verbose_name_plural = 'Локації розташування'

	def get_update_url(self):
		return reverse('directory_location_update',args=[self.id])

	def get_delete_url(self):
		return reverse('directory_location_delete',args=[self.id])

	def __str__(self):
		return '{} ({})'.format(self.name, self.address) 
		# Наприклад - "в/ч 3002 (м.Львів, вул.Княгині Ольги, 105)"


class Placement(models.Model):
	name = models.CharField(max_length=50,
							blank=False,
							null=False,
							verbose_name='Назва')
	location = models.ForeignKey(Location,
							on_delete=models.PROTECT,
							verbose_name='Локація')
	notes = models.CharField(max_length=2048,
							blank=True,
							null=True,
							verbose_name='Примітка')

	class Meta:
		verbose_name = 'Місце розташування'
		verbose_name_plural = 'Місця розташування'

	def get_update_url(self):
		return reverse('directory_placement_update',args=[self.id])

	def get_delete_url(self):
		return reverse('directory_placement_delete',args=[self.id])

	def __str__(self):
		return '{} ({})'.format(self.name, self.location.name) 
		# Наприклад - "Вузол зв'язку (в/ч 3002)"