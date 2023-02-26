from django.contrib import admin
from .models import Category, Equipment, Status

class EquipmentAdmin(admin.ModelAdmin):
	list_display = ('name', 'serialNumber','category', 'status', 'employee')
	list_filter = ('status', 'category', 'employee')
	search_fields = ('name', 'employee')
	ordering = ['name', 'status']
	list_editable = ('category', 'status', 'employee', 'serialNumber')


admin.site.register(Category)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Status)