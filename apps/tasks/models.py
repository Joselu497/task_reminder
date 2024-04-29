import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from apps.users.models import User

class Folder(models.Model):
    name = models.CharField(max_length=200)
    assigned_to = models.ForeignKey(User, on_delete = models.CASCADE, null = False)

    def __str__(self):
        return self.name

class Task(models.Model):    
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete = models.CASCADE, null = False)
    deadline = models.DateTimeField()
    priority = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    completed = models.BooleanField(default=False)
    folder_id = models.ForeignKey(Folder, on_delete = models.CASCADE, default = None, null = True)

    def __str__(self):
        return self.title
