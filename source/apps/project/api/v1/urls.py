from django.urls import path, include
from apps.project.api.v1.views import ProjectViewSet
from rest_framework import routers

app_name = 'project.api.v1'
router = routers.DefaultRouter()
router.register(r'', ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),

]
