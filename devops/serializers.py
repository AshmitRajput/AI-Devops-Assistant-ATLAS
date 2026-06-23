from rest_framework import serializers

from .models import (
    Build,
    Incident,
    IncidentAttempt,
    IncidentAnalysis
)

class BuildSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Build

        fields = "__all__"

class IncidentSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Incident

        fields = "__all__"

class IncidentAttemptSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = IncidentAttempt

        fields = "__all__"

class IncidentAnalysisSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = IncidentAnalysis

        fields = "__all__"

