from django.db import models
import uuid

from user.models import User

# Create your models here.
class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='managed_projects')
    members = models.ManyToManyField(User, related_name='projects', blank=True)

    class Meta:
        db_table = 'projects'
        ordering = ['-created_at']

        def __str__ (self) -> str:
            return self.title