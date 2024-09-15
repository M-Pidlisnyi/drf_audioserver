from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Track(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, null=True)
    track_file = models.FileField(null=True, blank=True, upload_to='tracks/', unique=True)

    def __str__(self):
        return f"{self.author} - {self.title}"

