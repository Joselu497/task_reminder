from django.contrib import admin

from .models import Folder, Task

admin.site.register(Task)
admin.site.register(Folder)

