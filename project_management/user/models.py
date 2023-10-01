from django.contrib.auth.models import AbstractUser
from django.db import models

import uuid

class User(AbstractUser):
    USER_ROLES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('member', 'Member'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField(max_length=10, choices=USER_ROLES, default='member')

