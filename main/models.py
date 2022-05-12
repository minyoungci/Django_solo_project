from ctypes import resize
from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse
from django_resized import ResizedImageField


class Category(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)

    # Utility Variable

    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updateed = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.title, self.uniqueId)

    def get_absolute_url(self):
        return reverse("category-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split("-")[4]
            self.slug = slugify("{} {}".format(self.title, self.uniqueId))

        self.slug = slugify("{} {}".format(self.title, self.uniqueId))
        self.last_updateed = timezone.localtime(timezone.now())
        super(Category, self).save(*args, **kwargs)


class Image(models.Model):
    description = models.TextField(null=True, blank=True)
    alttext = models.TextField(null=True, blank=True)
    hashtags = models.CharField(null=True, blank=True, max_length=300)

    # ImageFields

    squareImage = ResizedImageField(
        size=[1000, 1000],
        crop=["middle", "center"],
        default="default_square.jpg",
        upload_to="square",
    )
    landImage = ResizedImageField(
        size=[2878, 1618],
        crop=["middle", "center"],
        default="default_land.jpg",
        upload_to="landscape",
    )
    tallImage = ResizedImageField(
        size=[1618, 2878],
        crop=["middle", "center"],
        default="default_tall.jpg",
        upload_to="tall",
    )

    # RelatedFile

    category = models.CharField(null=True, blank=True, max_length=100)

    # Utility Variable

    uniquedId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.category.title, self.uniquedId)
