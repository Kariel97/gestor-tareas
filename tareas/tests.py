from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from tareas.models import Task

class TaskCreateTest(APITestCase):

    def setUp(self):
        """
        Crea un usuario y obtiene un token de acceso para usar en las pruebas.
        """
        self.user = User.objects.create_user(
            username='test',
            password='1234',
            email='test@example.com'
        )
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))

    def test_create_task(self):
        """
        Verifica que un usuario autenticado pueda crear una tarea.
        """
        url = '/api/tasks/create/'
        data = {
            'title': 'Tarea de ejemplo',
            'description': 'Descripción de la nueva tarea',
            'completed': False
        }
        response = self.client.post(url, data, format='json')
        
        # Verificar la respuesta
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, f"Response: {response.data}")

class TaskUpdateTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            password='1234',
            email='test@example.com'
        )
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))

        # Crear una tarea para el usuario
        self.task = Task.objects.create(
            title='Tarea de prueba',
            description='Descripción de la tarea',
            completed=False,
            user=self.user
        )

    def test_update_task(self):
        url = f'/api/tasks/{self.task.pk}/update/'
        data = {
            'title': 'Tarea actualizada',
            'description': 'Descripción actualizada',
            'completed': True
        }
        response = self.client.put(url, data, format='json')

        # Verificar la respuesta
        self.assertEqual(response.status_code, status.HTTP_200_OK, f"Response: {response.data}")

    def test_update_task_unauthorized(self):
        another_user = User.objects.create_user(
            username='anotheruser',
            password='anotherpassword123',
            email='anotheruser@example.com'
        )
        self.token = RefreshToken.for_user(another_user).access_token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))

        url = f'/api/tasks/{self.task.pk}/update/'
        data = {
            'title': 'Tarea actualizada por otro',
            'description': 'Descripción actualizada por otro',
            'completed': True
        }
        response = self.client.put(url, data, format='json')

        # Verificar la respuesta
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND, f"Response: {response.data}")

class TaskDeleteTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            password='1234',
            email='test@example.com'
        )
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))

        # Crear una tarea para el usuario
        self.task = Task.objects.create(
            title='Tarea de prueba',
            description='Descripción de la tarea',
            completed=False,
            user=self.user
        )

    def test_delete_task(self):
        url = f'/api/tasks/{self.task.pk}/delete/'
        response = self.client.delete(url)

        # Verificar la respuesta
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, f"Response: {response.data}")

    def test_delete_task_unauthorized(self):
        another_user = User.objects.create_user(
            username='anotheruser',
            password='anotherpassword123',
            email='anotheruser@example.com'
        )
        self.token = RefreshToken.for_user(another_user).access_token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))

        url = f'/api/tasks/{self.task.pk}/delete/'
        response = self.client.delete(url)

        # Verificar la respuesta
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND, f"Response: {response.data}")
