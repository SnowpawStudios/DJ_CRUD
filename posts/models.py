from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    featured_image = models.ImageField(null=True, blank=True, default='default.png')

    def __str__(self):
        return self.title


