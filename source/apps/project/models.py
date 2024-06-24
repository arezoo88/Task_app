from django.db import models
from django.utils.translation import gettext_lazy as _
from .constants import TASK_STATUS_CHOICES


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

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')


class Task(BaseModel):
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
        choices=TASK_STATUS_CHOICES,
        max_length=15,
        default='pending'
    )
    due_date = models.DateTimeField(
        verbose_name=_('Due_Date'),
    )

    def __str__(self):
        return self.title

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

    def __str__(self):
        return self.author

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
