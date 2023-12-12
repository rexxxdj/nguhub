from django.contrib import admin
from .models import Category, Status, Equipment, EquipmentDetail

'''
class EquipmentAdmin(admin.ModelAdmin):
	list_display = ('name', 'serial_number', 'category', 'status')
	list_filter = ('status', 'category')
	search_fields = ('name',)
	ordering = ['name', 'status']
	list_editable = ('category', 'status', 'serial_number')

class EquipmentDetailAdmin(admin.ModelAdmin):
	list_display = ('equipment__name', 'equipment__serial_number', 'location', 'placement', 'counterparty', 'responsible', 'employee','sender')
	list_filter = ('location', 'placement', 'counterparty', 'responsible', 'employee','sender')
	search_fields = ('equipment__name',)
	ordering = ['equipment__name', 'location', 'placement', 'counterparty', 'responsible', 'employee','sender']
	list_editable = ('location', 'placement', 'counterparty', 'responsible', 'employee','sender')


admin.site.register(Category)
admin.site.register(Status)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(EquipmentDetail, EquipmentDetailAdmin)
'''