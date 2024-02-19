from django.db import models

# Create your models here.
class Contributions(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True)
    image = models.FileField(upload_to="contribution_images/", blank=True)
