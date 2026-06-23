from django.contrib import admin

from .models import (
    Project,
    ProjectIntegration
)

admin.site.register(Project)

admin.site.register(ProjectIntegration)