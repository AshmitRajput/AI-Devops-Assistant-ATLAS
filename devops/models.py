from django.db import models
from projects.models import Project
from core.constants import (
    ATTEMPT_RESULT_CHOICES,
    ATTEMPT_RESULT_FAILED,
    BUILD_STATUS_CHOICES,
    BUILD_STATUS_RUNNING,
    INCIDENT_STATUS_CHOICES,
    INCIDENT_STATUS_OPEN,
)

# Create your models here.
class Build(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    build_number = models.IntegerField()

    status = models.CharField(
        max_length=20,
        choices=BUILD_STATUS_CHOICES,
        default=BUILD_STATUS_RUNNING
    )

    started_at = models.DateTimeField()

    completed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    raw_log = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

class Incident(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    build = models.ForeignKey(
        Build,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=INCIDENT_STATUS_CHOICES,
        default=INCIDENT_STATUS_OPEN
    )

    root_cause = models.TextField(
        blank=True
    )

    confidence_score = models.FloatField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    resolved_at = models.DateTimeField(
        null=True,
        blank=True
    )

class IncidentAttempt(models.Model):

    incident = models.ForeignKey(
        Incident,
        on_delete=models.CASCADE,
        related_name="attempts"
    )

    attempt_number = models.IntegerField()

    action_type = models.CharField(
        max_length=100
    )

    action_taken = models.TextField()

    result = models.CharField(
        max_length=20,
        choices=ATTEMPT_RESULT_CHOICES,
        default=ATTEMPT_RESULT_FAILED
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

class IncidentAnalysis(models.Model):

    incident = models.ForeignKey(
        Incident,
        on_delete=models.CASCADE,
        related_name="analyses"
    )

    analysis_text = models.TextField()

    suggested_fix = models.TextField()

    evidence = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

