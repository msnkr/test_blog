from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image   
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(default=timezone.now)
    images = models.ImageField(upload_to='post_media', blank=True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


    def save(self):
        super().save()
        img = Image.open(self.images.path)
        if img.width > 1000 and img.height > 550 or img.width < 1000 and img.height < 550:
            out = (1000, 550)
            img.thumbnail(out)
            img.save(self.images.path)