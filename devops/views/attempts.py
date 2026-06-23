from rest_framework.views import ( APIView )
from rest_framework.permissions import ( IsAuthenticated )
from rest_framework.response import ( Response )
from devops.models import ( Incident, IncidentAttempt )
from devops.serializers import ( IncidentAttemptSerializer )
from devops.services import ( get_next_attempt_number )

class AddAttemptView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def post(
        self,
        request,
        incident_id
    ):

        incident = (
            Incident.objects.get(
                id=incident_id
            )
        )

        data = request.data.copy()

        data[
            "incident"
        ] = incident.id

        data[
            "attempt_number"
        ] = (
            get_next_attempt_number(
                incident
            )
        )

        serializer = (
            IncidentAttemptSerializer(
                data=data
            )
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            serializer.data
        )