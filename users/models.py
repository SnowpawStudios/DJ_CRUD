from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username =models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to = 'profiles/', default='profiles/default.png')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)

