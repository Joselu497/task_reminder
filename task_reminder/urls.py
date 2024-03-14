from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(('apps.users.urls', 'users'), namespace='users')),
    path('', include(('apps.tasks.urls', 'tasks'), namespace='tasks')),
]
