from celery import shared_task
from django.utils import timezone
from django.core.mail import send_mail
from apps.project.models import Task, Project
from django.template.loader import render_to_string


@shared_task
def send_task_reminders():
    # Get tasks due within the next 24 hours
    tasks = Task.objects.filter(
        due_date__lte=timezone.now() + timezone.timedelta(days=1))

    for task in tasks:
        subject = f'Reminder: Task "{task.title}" is due soon!'
        message = f'Dear arezoo,\n\nThis is a reminder that task "{task.title}" is due on {task.due_date}.\n\nRegards,\nYour Task Management Team'
        recipient_list = ['arezoo.darvish6969@gmail.com']

        send_mail(subject, message, None, recipient_list)

@shared_task
def send_daily_project_summary():
    projects = Project.objects.all()
    report = render_to_string(
        'email_templates/daily_summary.html', {'projects': projects})
    subject = 'Daily Project Summary Report'
    recipient_list = ['arezoo.darvish6969@gmail.com']
    send_mail(subject, report, None, recipient_list)
