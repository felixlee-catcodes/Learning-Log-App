from django.db import models

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)    
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Holds extra info for managing the model."""
        # Set special attribute to tell Django how to pluralize the model's name:
        verbose_name_plural = 'entries'

    def __str__(self):
        """return a string representation of the model."""
        return f'{self.text[:50]}...'    