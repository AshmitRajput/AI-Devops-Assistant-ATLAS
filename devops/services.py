from .models import (Incident)
from core.constants import (INCIDENT_STATUS_RESOLVED)

def resolve_incident( incident ):
    incident.status = ( INCIDENT_STATUS_RESOLVED )
    incident.save()
    return incident

def get_next_attempt_number( incident ):
    count = ( incident.attempts.count() )
    return count + 1

