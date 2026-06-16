from django.db import models
from django.contrib.auth.models import (
    AbstractUser
)
from .managers import UserManager
from core.constants import (
    USER_STATUS_ACTIVE,
    USER_STATUS_CHOICES
)


class User(AbstractUser):
    objects = UserManager()
    username = None
    email = models.EmailField(
        unique=True
    )

    first_name = models.CharField(
        max_length=100,
        blank=True
    )

    last_name = models.CharField(
        max_length=100,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=USER_STATUS_CHOICES,
        default=USER_STATUS_ACTIVE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email