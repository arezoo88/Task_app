from rest_framework import viewsets, status
from apps.project.models import Project, Task, Comment
from apps.project.api.v1.serializers import ProjectSerializer, TaskSerializer, CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.conf import settings
from django.core.cache import cache

CACHE_TTL = getattr(settings, 'CACHE_TTL', 60 * 15)


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def list(self, request, *args, **kwargs):
        cache_key = 'projects_list'
        cached_projects = cache.get(cache_key)

        if cached_projects:
            return Response(cached_projects)
        serializer = self.get_serializer(self.queryset, many=True)
        cache.set(cache_key, serializer.data, CACHE_TTL)

        return Response(serializer.data)


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(task__pk=self.kwargs['id'])

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['task'] = self.kwargs.get('id')
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
