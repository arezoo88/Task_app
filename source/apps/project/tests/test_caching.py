
from django.test import TestCase
from rest_framework.test import APIClient
from django.core.cache import cache
from apps.project.models import Project, Task
from django.utils import timezone


class CachingTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.project_data = {'name': 'Test Project'}
        self.project = Project.objects.create(**self.project_data)
        self.project_list_url = '/api/v1/projects/'
        self.project_detail_url = f'/api/v1/projects/{self.project.pk}/'

    def test_project_list_caching(self):
        # Clear cache before test
        cache.delete('projects_list')
        # First request to list projects (cache should be empty)
        response = self.client.get(self.project_list_url)
        self.assertEqual(response.status_code, 200)

        # Cache should be set after the first request
        cached_projects = cache.get('projects_list')
        self.assertIsNotNone(cached_projects)
        self.assertEqual(cached_projects, response.json())

    def test_project_create_invalidates_cache(self):
        # Ensure cache is set
        self.client.get(self.project_list_url)
        self.assertIsNotNone(cache.get('projects_list'))

        # Create a new project
        response = self.client.post(self.project_list_url, self.project_data)
        self.assertEqual(response.status_code, 201)

        # Cache should be invalidated
        self.assertIsNone(cache.get('projects_list'))

    def test_project_update_invalidates_cache(self):
        # Ensure cache is set
        self.client.get(self.project_list_url)
        self.assertIsNotNone(cache.get('projects_list'))

        # Update the project
        response = self.client.patch(
            self.project_detail_url, {'title': 'Updated Project'})
        self.assertEqual(response.status_code, 200)

        # Cache should be invalidated
        self.assertIsNone(cache.get('projects_list'))

    def test_project_delete_invalidates_cache(self):
        # Ensure cache is set
        self.client.get(self.project_list_url)
        self.assertIsNotNone(cache.get('projects_list'))

        # Delete the project
        response = self.client.delete(self.project_detail_url)
        self.assertEqual(response.status_code, 204)

        # Cache should be invalidated
        self.assertIsNone(cache.get('projects_list'))


class TaskViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.project = Project.objects.create(name='Test Project')
        self.task_data = {'title': 'Test Task',
                          'project': self.project, 'due_date': timezone.now()}
        self.task = Task.objects.create(**self.task_data)
        self.task_list_url = '/api/v1/tasks/'
        self.task_detail_url = lambda pk: f'/api/v1/tasks/{pk}/'

    def test_task_list_caching(self):
        # Clear cache before test
        cache.delete('tasks_list')
        # First request to list projects (cache should be empty)
        response = self.client.get(self.task_list_url)
        self.assertEqual(response.status_code, 200)

        # Cache should be set after the first request
        cached_tasks = cache.get('tasks_list')
        self.assertIsNotNone(cached_tasks)
        self.assertEqual(cached_tasks, response.json())
    