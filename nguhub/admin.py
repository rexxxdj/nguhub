from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .models import Location

admin.site.register(Location)
admin.site.register(LogEntry)