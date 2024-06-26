from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from apps.project.models import Project, Task
from django.core.cache import cache
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@receiver(post_save, sender=Project)
@receiver(post_delete, sender=Project)
def invalidate_project_cache(sender, instance, **kwargs):
    cache.delete('projects_list')


@receiver(post_save, sender=Task)
@receiver(post_delete, sender=Task)
def invalidate_task_cache(sender, instance, **kwargs):
    cache.delete('tasks_list')


channel_layer = get_channel_layer()


@receiver(post_save, sender=Task)
@receiver(post_delete, sender=Task)
@receiver(post_save, sender=Project)
@receiver(post_delete, sender=Project)
def send_notification(sender, instance, **kwargs):
    if kwargs.get('created') or kwargs.get('deleted'):
        async_to_sync(channel_layer.group_send)(
            'notifications_group',
            {
                'type': 'send_notification',
                'message': f'{sender.__name__} {instance.id} has been {kwargs.get("created", "deleted")}.'
            }
        )
