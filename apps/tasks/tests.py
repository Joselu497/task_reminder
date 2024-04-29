from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .views import CompleteTask
from .models import Task
from apps.users.models import User

class CompleteTaskTestCase(TestCase):
    def test_complete_task(self):
        user = User.objects.create(
            username='Test User',
            email='testuser@gmail.com',
            password='password')
        task = Task.objects.create(
            title='Test Task', 
            description='Test Description', 
            assigned_to=user,
            deadline='2024-03-31T12:00:00Z',
            priority=2,
            completed=False)
        view = CompleteTask.as_view()
        factory = APIRequestFactory()
        request = factory.put(f'/tasks/{task.id}/complete/')
        response = view(request, task_id=task.id)
        
        self.assertEqual(response.status_code, 200)
        task.refresh_from_db()
        self.assertEqual(task.completed, True)
