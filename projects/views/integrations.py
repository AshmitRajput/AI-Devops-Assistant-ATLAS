from rest_framework.views import APIView

from rest_framework.permissions import (
    IsAuthenticated
)

from rest_framework.response import (
    Response
)

from projects.models import (
    Project,
    ProjectIntegration
)

from projects.serializers import (
    ProjectIntegrationSerializer
)


class ProjectIntegrationView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def post(
        self,
        request,
        project_id
    ):

        project = Project.objects.get(
            id=project_id,
            user=request.user
        )

        integration, _ = (
            ProjectIntegration.objects.get_or_create(
                project=project
            )
        )

        serializer = (
            ProjectIntegrationSerializer(
                integration,
                data=request.data,
                partial=True
            )
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            serializer.data
        )