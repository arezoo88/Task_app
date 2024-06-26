from rest_framework import serializers
from apps.project.models import Project, Task, Comment


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # data['project'] = ProjectSerializer(
        #     Project.objects.get(pk=instance.project.pk)).data
        return data


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
