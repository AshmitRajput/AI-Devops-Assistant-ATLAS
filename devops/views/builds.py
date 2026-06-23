from rest_framework import ( viewsets )
from rest_framework.permissions import ( IsAuthenticated )
from devops.models import Build
from devops.serializers import ( BuildSerializer )

class BuildViewSet(
    viewsets.ModelViewSet
):

    serializer_class = BuildSerializer

    permission_classes = [
        IsAuthenticated
    ]

    queryset = Build.objects.all()