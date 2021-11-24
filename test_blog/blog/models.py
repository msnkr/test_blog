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
    date_published = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.post_image.path)
    #     output_size = (1000, 700)
    #     img.resize(output_size)
    #     img.save(self.post_image.path)
    