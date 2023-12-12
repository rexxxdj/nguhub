from django.db import models
from django.urls import reverse
from django.conf import settings
from simple_history.models import HistoricalRecords
from phonenumber_field.modelfields import PhoneNumberField

from nguhub.models import Placement


class ActionPost(models.Model):
	name = models.CharField(max_length=30,
						verbose_name='Назва')
	notes = models.CharField(max_length=255,
						verbose_name = 'Додаткові відомості')

	class Meta:
		verbose_name = 'Бойовий пост'
		verbose_name_plural = 'Бойові пости'

	def get_update_url(self):
		return reverse('directory_actionpost_update', args=[self.id])

	def get_delete_url(self):
		return reverse('directory_actionpost_delete', args=[self.id])

	def __str__(self):
		return '{} ({})'.format(self.name, self.notes)


class Employee(models.Model):
	def directory_path(instance, filename):
		return 'media/employee/{0}/{1}'.format(instance.id, filename)


	RANK_CHOICES = (
        (u"сл.", u"Службовець"),
        (u"солд.", u"Солдат"),
        (u"ст.солд.", u"Старший солдат"),
        (u"мол.с-нт", u"Молодший сержант"),
        (u"с-нт", u"Сержант"),
        (u"ст.с-нт", u"Старший сержант"),
        (u"гол.с-нт", u"Головний сержант"),
        (u"шт.с-нт", u"Штаб-сержант"),
        (u"м.с-нт", u"Майстер-сержант"),
        (u"ст.м.с-нт", u"Старший майстер-сержант"),
        (u"гол.м.с-нт", u"Головний майстер-сержант"),
        (u"мол.л-нт", u"Молодший лейтенант"),
        (u"л-нт", u"Лейтенант"),
        (u"ст.л-нт", u"Старший лейтенант"),
        (u"к-н", u"Капітан"),
        (u"м-р", u"Майор"),
        (u"п/п-к", u"Підполковник"),
        (u"п-к", u"Полковник"),
        (u"бриг.ген.", u"Бригадний генерал"),
        (u"ген.м-р", u"Генерал-майор"),
        (u"ген.л-нт", u"Генерал-лейтенант"),
        (u"ген.", u"Генерал")
    )

	placement = models.ForeignKey(Placement,
							on_delete=models.PROTECT,
							verbose_name='Локація користувача')
	rank = models.CharField(max_length=30, 
							choices=RANK_CHOICES, 
							blank=False, 
							null=False, 
							verbose_name='Звання')
	firstname = models.CharField(max_length=15,
							blank=False, 
							null=False, 
							verbose_name="Ім'я")
	lastname = models.CharField(max_length=25,
							blank=False, 
							null=False, 
							verbose_name='Прізвище')
	surname = models.CharField(max_length=25,
							blank=True, 
							null=True, 
							verbose_name='По батькові')
	position = models.CharField(max_length=100,
							blank=False, 
							null=False, 
							verbose_name='посада')
	notes = models.CharField(max_length=1024,
							blank=True, 
							null=True, 
							verbose_name='Додатковий коментар')
	officialPhone = models.CharField(max_length=10, 
							blank=True, 
							null=True, 
							verbose_name='Службовий номер телефону')
	personalPhone = PhoneNumberField(blank=True, 
							null=True, 
							unique=True)
	photo = models.ImageField(upload_to=directory_path, 
							blank=True, 
							null=True,
							verbose_name='Фотографія')
	is_operator = models.BooleanField(
							null = True,
							default = True,
							verbose_name = u'Зв\'язківець')
	actionPost = models.ManyToManyField(ActionPost,
							verbose_name = 'Бойовий пост')
	history = HistoricalRecords()

	class Meta:
		verbose_name = 'Співробітник'
		verbose_name_plural = 'Співробітники'

	def get_absolute_url(self):
		return reverse('employee:detail',
			args=[self.id])

	def get_update_url(self):
		return reverse('employee:update',
			args=[self.id])

	def get_delete_url(self):
		return reverse('employee:delete',
			args=[self.id])

	def fullname(self):
		return '{} {}'.format(self.lastname, self.firstname)

	def shortname(self):
		if self.surname is None:
			surname = ''
		else :
			surname = self.surname[0]
		return '{} {}.{}.'.format(self.lastname, self.firstname[0],surname)

	def shortposition(self):
		pos = ''
		for i in self.position.split(" "):
			pos = pos + i[0]
		return pos.upper()

	def __str__(self):
		return '{} {}'.format(self.lastname, self.firstname)