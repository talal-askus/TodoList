from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Todo


class TodoListApiViewTest(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        
        # Create a todo item
        self.todo = Todo.objects.create(task="Test Task", completed=False, user=self.user)

    def test_get_todos(self):
        # Test retrieving todos
        url = reverse('todo-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming there's one todo item

    def test_create_todo(self):
        # Test creating a new todo
        url = reverse('todo-list')
        data = {'task': 'New Task', 'completed': False}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_todo(self):
        # Test updating an existing todo
        url = reverse('todo-detail', kwargs={'pk': self.todo.pk})
        data = {'task': 'Updated Task', 'completed': True}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_todo(self):
        # Test deleting a todo
        url = reverse('todo-detail', kwargs={'pk': self.todo.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)