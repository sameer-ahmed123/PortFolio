from django.db import models
from django.utils.text import slugify
import random

# django-taggit https://django-taggit.readthedocs.io/en/latest/
from taggit.managers import TaggableManager

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500, blank=True, null=True)
    description = models.TextField()
    type = models.CharField(max_length=260)
    url = models.URLField(max_length=1000)
    # django-taggit.
    tags = TaggableManager(blank=True)

    def save(self, *args, **kwargs):
        random_number = random.randint(1, 100000)
        if not self.slug:
            self.slug = slugify(f"{self.title} {random_number}")
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title




class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"