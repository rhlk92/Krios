from django.db import models

class Task(models.Model):
    description = models.CharField(max_length=30)
    completed = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now_add=True)
