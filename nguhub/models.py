from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords


class Location(models.Model):
	name = models.CharField(max_length=50,
							blank=False,
							null=False,
							verbose_name='Місце закріплення')
	delete_reason=models.CharField(max_length=50,
							blank=True, 
							null=True, 
							verbose_name='Причина видалення')
	history = HistoricalRecords()

	class Meta:
		verbose_name = 'Місце закріплення'
		verbose_name_plural = 'Місце закріплення'

	def get_update_url(self):
		return reverse('directory_other_location_update',
			args=[self.id])

	def get_delete_url(self):
		return reverse('directory_other_location_delete',
			args=[self.id])

	def __str__(self):
		return self.name # Наприклад - Вузол зв'язку, Склад НЗ і т.д.


class CurrentLocation(models.Model):
	name = models.CharField(max_length=50,
							blank=False,
							null=False,
							verbose_name='Місце знаходження')
	delete_reason=models.CharField(max_length=50,
							blank=True, 
							null=True, 
							verbose_name='Причина видалення')
	history = HistoricalRecords()

	class Meta:
		verbose_name = 'Поточне місцезнаходження'
		verbose_name_plural = 'Поточне місцезнаходження'

	def get_update_url(self):
		return reverse('directory_other_currentlocation_update',
			args=[self.id])

	def get_delete_url(self):
		return reverse('directory_other_currentlocation_delete',
			args=[self.id])

	def __str__(self):
		return self.name # Наприклад - Вузол зв'язку, Склад НЗ і т.д.