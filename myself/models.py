from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    duration = models.CharField(max_length=10, blank=True, null=True)
    flow = models.CharField(max_length=10, blank=True, null=True)
    skin_type = models.CharField(max_length=20, blank=True, null=True)
    itchiness = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
