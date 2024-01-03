from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_LEVEL = (
        ("CR", 'Criador'),
        ("ED", 'Editor'),
        ("SP", 'Supervisor'),
    )

    usuario = models.CharField(max_length=2, blank=True, choices=USER_LEVEL, default='CR', )

    def __str__(self):
        return self.username
