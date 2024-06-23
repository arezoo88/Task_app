from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from apps.project.models import Project, Task
from django.core.cache import cache


@receiver(post_save, sender=Project)
@receiver(post_delete, sender=Project)
def invalidate_project_cache(sender, instance, **kwargs):
    cache.delete('projects_list')


@receiver(post_save, sender=Task)
@receiver(post_delete, sender=Task)
def invalidate_task_cache(sender, instance, **kwargs):
    cache.delete('tasks_list')
