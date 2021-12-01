from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    completed = models.BooleanField(default=False)
    updated = models.BooleanField(default=False)

    def __str__(self):
        return self.task
