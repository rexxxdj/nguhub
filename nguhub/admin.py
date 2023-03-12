from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .models import Location, CurrentLocation

admin.site.register(Location)
admin.site.register(CurrentLocation)
admin.site.register(LogEntry)