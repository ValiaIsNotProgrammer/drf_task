from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
