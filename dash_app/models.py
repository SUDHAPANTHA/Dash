from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    tags = models.CharField(max_length=200)
    featured_image = models.ImageField(upload_to='post_images/', null=True, blank=True)

    def __str__(self):
        return self.title
