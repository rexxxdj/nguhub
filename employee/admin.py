from django.contrib import admin

from .models import ActionPost, Employee, MonthJournal


admin.site.register(ActionPost)
admin.site.register(Employee)
admin.site.register(MonthJournal)