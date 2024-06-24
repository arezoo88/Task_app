from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Project, Task, Comment
from django.utils import timezone


class ProjectTests(APITestCase):
    def setUp(self):
        self.project = Project.objects.create(name="Test Project")
        self.project_list_url = '/api/v1/projects/'
        self.project_detail_url = f'/api/v1/projects/{self.project.pk}/'

    def test_list_projects(self):
        response = self.client.get(self.project_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_project(self):
        response = self.client.get(self.project_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_project(self):
        data = {'name': 'New Project'}
        response = self.client.post(self.project_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_project(self):
        data = {'name': 'Updated Project'}
        response = self.client.put(self.project_detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_project(self):
        response = self.client.delete(self.project_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TaskViewSetTests(APITestCase):

    def setUp(self):
        self.project = Project.objects.create(name="Test Project")
        self.task_list_url = '/api/v1/tasks/'
        self.task_detail_url = lambda pk: f'/api/v1/tasks/{pk}/'
        self.task = Task.objects.create(
            title="Test Task", project=self.project, due_date=timezone.now())

    def test_list_tasks(self):
        response = self.client.get(self.task_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_task(self):
        response = self.client.get(self.task_detail_url(self.task.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        data = {'title': 'New Task', 'project': self.project.pk,
                'due_date': timezone.now()}
        response = self.client.post(self.task_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_pathch_task(self):
        data = {'name': 'Updated Task', 'project': self.project.pk, }
        response = self.client.patch(self.task_detail_url(self.task.pk), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        response = self.client.delete(self.task_detail_url(self.task.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CommentViewSetTests(APITestCase):

    def setUp(self):
        self.project = Project.objects.create(name="Test Project")
        self.task = Task.objects.create(
            title="Test Task", project=self.project, due_date=timezone.now())
        self.comment_list_create_url = f'/api/v1/tasks/{self.task.pk}/comments/'
        self.comment = Comment.objects.create(
            content="Test Comment", task=self.task, author='Arezoo Darvishi')

    def test_list_comments(self):
        response = self.client.get(self.comment_list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['content'], "Test Comment")

    def test_create_comment(self):
        data = {'content': 'New Comment',
                'task': self.task, 'author': 'Arezoo Darvishi'}
        response = self.client.post(self.comment_list_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 2)

    def test_create_comment_with_missing_content(self):
        data = {'task': self.task, 'author': 'Arezoo Darvishi'}
        response = self.client.post(self.comment_list_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
