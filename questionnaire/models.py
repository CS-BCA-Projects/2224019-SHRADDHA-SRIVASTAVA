from django.db import models

class UserProfile(models.Model):
    skin_type = models.CharField(max_length=50)
    
    def __str__(self):
        return self.skin_type
