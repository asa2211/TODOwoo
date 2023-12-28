from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    CHOICES = (
        (3, 'admin'),
        (1, 'user'),
        (2, "manager")
    )
    roles = models.PositiveSmallIntegerField(default=1, choices=CHOICES)


class ToDoModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
