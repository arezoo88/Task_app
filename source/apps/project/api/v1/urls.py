from django.urls import path, include
from apps.project.api.v1.views import ProjectViewSet, TaskViewSet
from rest_framework import routers

app_name = 'project.api.v1'
router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]
