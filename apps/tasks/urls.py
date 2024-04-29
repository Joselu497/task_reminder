from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import FolderViewSet, TaskViewSet
from .views import CompleteTask

router = DefaultRouter()
router.register(r'folders', FolderViewSet, basename='folders')
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),

    path('tasks/<uuid:task_id>/complete/', CompleteTask.as_view(), name='complete_task'),
]