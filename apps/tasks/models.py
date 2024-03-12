from django.apps import apps
from django.db import models
from apps.users.models import User

class Task(models.Model):    
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete = models.CASCADE)
    deadline = models.DateTimeField()
    priority = models.IntegerField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
