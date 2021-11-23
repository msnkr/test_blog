from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    post_image = models.ImageField(upload_to='post_media')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title