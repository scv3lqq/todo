from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = None
    last_name = None

    def get_absolute_url(self):
        return f"{self.pk}"
