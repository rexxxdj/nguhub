from django.contrib import admin
from .models import Category, Element, Status

class ElementAdmin(admin.ModelAdmin):
	list_display = ('name', 'serialNumber','location','category', 'status', 'value', 'equipment')
	list_filter = ('status', 'category','location')
	search_fields = ('name', 'serialNumber', 'equipment')
	ordering = ['name', 'status','location']
	list_editable = ('category','location', 'status', 'equipment', 'serialNumber', 'value')


admin.site.register(Category)
admin.site.register(Element, ElementAdmin)
admin.site.register(Status)