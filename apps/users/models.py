from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=80)
    password = models.CharField()
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name