from rest_framework import viewsets
from apps.project.models import Project
from apps.project.api.v1.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
