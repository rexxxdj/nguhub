from django.contrib import admin
from .models import Category, Element, Status

class ElementAdmin(admin.ModelAdmin):
	list_display = ('name', 'serialNumber','category', 'status', 'value', 'equipment')
	list_filter = ('status', 'category')
	search_fields = ('name', 'serialNumber', 'equipment')
	ordering = ['name', 'status']
	list_editable = ('category', 'status', 'equipment', 'serialNumber', 'value')


admin.site.register(Category)
admin.site.register(Element, ElementAdmin)
admin.site.register(Status)