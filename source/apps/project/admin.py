from django.contrib import admin
from apps.project.models import Project, Task, Comment


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name',)


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'comment_count')
    inlines = [CommentInline]

    def comment_count(self, obj):
        return obj.comments.count()
    comment_count.short_description = 'Comment Count'


admin.site.register(Task, TaskAdmin)
admin.site.register(Project, ProjectAdmin)
