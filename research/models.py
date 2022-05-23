from distutils.command.upload import upload
from django.db import models


class Research(models.Model):

    title = models.CharField(max_length=100, blank=True)
    description = models.TextField()

    file = models.ImageField(upload_to="research_image")
    caption = models.TextField()
