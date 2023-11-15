from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """
    Post model for each post that a authenticated user
    creates.
    Default Image set from Cloudinary
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='../default_post_ylpvmf',
        blank=True
    )

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return f'{self.id} {self.title}'