from rest_framework import ( viewsets )
from rest_framework.permissions import ( IsAuthenticated )
from devops.models import ( Incident )
from devops.serializers import ( IncidentSerializer )

class IncidentViewSet(
    viewsets.ModelViewSet
):

    serializer_class = (
        IncidentSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]

    queryset = (
        Incident.objects.all()
    )