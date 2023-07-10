from django.contrib import admin
from django.contrib.admin.models import LogEntry

from .models import Location, Placement


admin.site.register(Location)
admin.site.register(Placement)
admin.site.register(LogEntry)