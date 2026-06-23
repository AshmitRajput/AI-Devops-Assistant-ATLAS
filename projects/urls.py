from django.urls import path

from rest_framework.routers import (
    DefaultRouter
)

from projects.views.projects import (
    ProjectViewSet
)

from projects.views.integrations import (
    ProjectIntegrationView
)

router = DefaultRouter()

router.register(
    "",
    ProjectViewSet,
    basename="projects"
)

urlpatterns = router.urls

urlpatterns += [

    path(
        "<int:project_id>/integrations/",
        ProjectIntegrationView.as_view()
    ),

]