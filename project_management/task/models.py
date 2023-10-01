from django.db import models
import uuid

from project.models import Project
from user.models import User

class Task(models.Model):
    STATUS_CHOICES = (
        ('todo', 'Todo'),
        ('inprogress', 'In Progress'),
        ('inreview', 'In Review'),
        ('done', 'Done'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks', blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')



    class Meta:
        db_table = 'tasks'
        ordering = ['-created_at']

        def __str__ (self) -> str:
            return self.title