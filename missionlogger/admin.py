from django.contrib import admin
from .models import Vessel, Mission


class VesselAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')


class MissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'vessel', 'status', 'created_at', 'updated_at')


admin.site.register(Vessel, VesselAdmin)
admin.site.register(Mission, MissionAdmin)
