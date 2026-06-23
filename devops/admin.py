from django.contrib import admin

from .models import (
    Build,
    Incident,
    IncidentAttempt,
    IncidentAnalysis
)

admin.site.register(Build)
admin.site.register(Incident)
admin.site.register(IncidentAttempt)
admin.site.register(IncidentAnalysis)