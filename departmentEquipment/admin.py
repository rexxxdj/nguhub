from django.contrib import admin
from .models import Category, Equipment, Status

class EquipmentAdmin(admin.ModelAdmin):
	list_display = ('name', 'serialNumber','location','category', 'status', 'employee')
	list_filter = ('status', 'category', 'employee','location')
	search_fields = ('name', 'employee')
	ordering = ['name', 'status','location']
	list_editable = ('category','location', 'status', 'employee', 'serialNumber')


admin.site.register(Category)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Status)