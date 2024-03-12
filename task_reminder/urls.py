from django.contrib import admin
from django.db import router
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.tasks.views import TaskViewSet
from apps.users.views import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include((router.urls, 'users'), namespace='users')),
    path('', include((router.urls, 'tasks'), namespace='tasks')),
]
