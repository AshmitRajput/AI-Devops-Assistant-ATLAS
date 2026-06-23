from django.urls import ( path, include )
from rest_framework.routers import ( DefaultRouter )
from devops.views.builds import ( BuildViewSet )
from devops.views.incidents import ( IncidentViewSet )
from devops.views.attempts import ( AddAttemptView )
from devops.views.analysis import ( ResolveIncidentView )

router = DefaultRouter()

router.register(
    "builds",
    BuildViewSet
)

router.register(
    "incidents",
    IncidentViewSet
)

urlpatterns = [
    path(
        "",
        include(
            router.urls
        )
    ),
    path(
        "incidents/<int:incident_id>/attempt/",
        AddAttemptView.as_view()
    ),
    path(
        "incidents/<int:incident_id>/resolve/",
        ResolveIncidentView.as_view()
    ),
]