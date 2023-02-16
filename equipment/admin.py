from django.contrib import admin
from .models import Category, Equipment, Status


admin.site.register(Category)
admin.site.register(Equipment)
admin.site.register(Status)