from django.db import models
from users.models import Profile
# Create your models here.

class Post(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    featured_image = models.ImageField(null=True, blank=True, default='default.png')

    def __str__(self):
        return self.title


