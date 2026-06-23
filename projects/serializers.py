from rest_framework import serializers

from .models import (
    Project,
    ProjectIntegration
)


class ProjectSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Project

        fields = "__all__"

        read_only_fields = (
            "user",
            "created_at",
            "updated_at",
        )


class ProjectIntegrationSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = ProjectIntegration

        exclude = []