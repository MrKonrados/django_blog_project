from unidecode import unidecode

from django.db import models
from django.template.defaultfilters import slugify


class Post(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    content = models.TextField()

    # create slug
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(unidecode(self.title))
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)


class User(models.Model):
    username = models.CharField(max_length=250)  # TODO: musi być unikalny
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)

    def __str__(self):
        return str(self.first_name + " " + self.last_name)
