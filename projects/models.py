from django.db import models
from django.conf import settings

class Project(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="projects"
    )

    name = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name


class ProjectIntegration(models.Model):

    project = models.OneToOneField(
        Project,
        on_delete=models.CASCADE,
        related_name="integration"
    )

    github_repo = models.CharField(
        max_length=500,
        blank=True
    )

    github_token = models.TextField(
        blank=True
    )

    jenkins_url = models.CharField(
        max_length=500,
        blank=True
    )

    jenkins_username = models.CharField(
        max_length=255,
        blank=True
    )

    jenkins_token = models.TextField(
        blank=True
    )

    aws_access_key = models.TextField(
        blank=True
    )

    aws_secret_key = models.TextField(
        blank=True
    )

    aws_region = models.CharField(
        max_length=100,
        blank=True
    )

    kubeconfig_file = models.FileField(
        upload_to="kubeconfigs/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.project.name} Integration"