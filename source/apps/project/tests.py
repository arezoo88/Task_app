from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Project, Task, Comment


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
