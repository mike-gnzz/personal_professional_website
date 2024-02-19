from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    image = models.FileField(upload_to="project_images/", blank=True)

class Contributions(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True)
    main_image = models.FileField(upload_to="contribution_images/", blank=True)
    detail_images = models.ManyToManyField("DetailImage", blank=True)

class Detailimage(models.Model):
    image = models.FileField(upload_to="detail_files/")

