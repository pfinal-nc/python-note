from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=30)
    content = models.TextField()
    add_time = models.DateField()

    def __str__(self):
        return self.title
