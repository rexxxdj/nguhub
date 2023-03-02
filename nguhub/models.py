from django.db import models
from simple_history.models import HistoricalRecords


class Location(models.Model):
	name = models.CharField(max_length=50,
							blank=False,
							null=False,
							verbose_name='Місце закріплення комплектуючих')
	history = HistoricalRecords()

	class Meta:
		verbose_name = 'Місце закріплення комплектуючих'
		verbose_name_plural = 'Місце закріплення комплектуючих'

	def __str__(self):
		return self.name # Наприклад - Вузол зв'язку, Склад НЗ і т.д.