from django.db import models
import datetime

# Create your models here.
class Content(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    author = models.ForeignKey(
    	'auth.User',
    	on_delete = models.CASCADE,
    	)
    title = models.TextField()
    description = models.CharField(max_length=255)
    def __str__(self):
        """A string representation of the model."""
        return self.title