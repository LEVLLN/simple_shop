from django.db import models
import datetime

# Create your models here.
class Content(models.Model):
    text = models.TextField()
    
    author = models.ForeignKey(
    	'auth.User',
    	on_delete = models.CASCADE,
    	)
    title = models.TextField()
    description = models.CharField(max_length=255)
    def __str__(self):
        """A string representation of the model."""
        return self.title
