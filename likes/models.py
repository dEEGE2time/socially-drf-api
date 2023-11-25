from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Like(models.Model):
    """
    The likes model for users to like posts.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        #unique_together, prevent user to like the same post twice.
        unique_together = ['owner', 'post']
    
    def __str__(self):
        return f'{self.owner} {self.post}'
