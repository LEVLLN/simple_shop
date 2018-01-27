from django.db import models

# Create your models here.
class Content(models.Model):
    text = models.TextField()
    def __str__(self):
        """A string representation of the model."""
        return 'text: ' + self.text[:50]