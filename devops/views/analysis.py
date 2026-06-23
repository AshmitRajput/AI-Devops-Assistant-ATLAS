from rest_framework.views import ( APIView )
from rest_framework.permissions import ( IsAuthenticated )
from rest_framework.response import ( Response )
from devops.models import ( Incident )
from devops.services import ( resolve_incident )

class ResolveIncidentView( APIView ):

    permission_classes = [
        IsAuthenticated
    ]

    def post( self, request, incident_id ):
        incident = (
            Incident.objects.get( id=incident_id )
        )
        incident = (
            resolve_incident( incident )
        )

        return Response(
            {
                "message":
                "Incident resolved"
            }
        )