from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name=_('Created_at'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_('Updated_at'),
        auto_now=True
    )

    class Meta:
        abstract = True


class Project(BaseModel):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=255
    )
    description = models.TextField(
        verbose_name=_('Description'),
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')


class Task(BaseModel):
    STATUS_CHOICES = {
        "pending": "Pending",
        "in_progress": "In Progress",
        "completed": "Completed"
    }
    project = models.ForeignKey(
        verbose_name=_('Project'),
        to=Project,
        related_name='tasks',
        on_delete=models.CASCADE
    )
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=255
    )
    description = models.TextField(
        verbose_name=_('Description'),
        blank=True,
        null=True
    )
    status = models.CharField(
        verbose_name=_('Status'),
        choices=STATUS_CHOICES,
        max_length=15,
        default='pending'
    )
    due_date = models.DateTimeField(
        verbose_name=_('Due_Date'),
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')


class Comment(models.Model):
    task = models.ForeignKey(
        verbose_name=_('Task'),
        to=Task,
        related_name='comments',
        on_delete=models.CASCADE
    )
    author = models.CharField(
        verbose_name=_('Author'),
        max_length=255
    )
    content = models.TextField(
        verbose_name=_('Content')
    )
    created_at = models.DateTimeField(
        verbose_name=_('Created_at'),
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
