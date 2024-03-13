from django.db import models

class User(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name