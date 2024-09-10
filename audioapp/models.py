from django.db import models

# Create your models here.
class Track(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.author} - {self.title}"
