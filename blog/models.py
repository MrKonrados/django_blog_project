from unidecode import unidecode

from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

class Post(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True, max_length=250)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    image = models.ImageField(upload_to="images/%Y/%m/", blank=True, null=True)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug, })

    # create slug
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(unidecode(self.title))
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)


class Author(models.Model):
    username = models.CharField(max_length=250)  # TODO: musi być unikalny
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)

    def __str__(self):
        return str(self.first_name + " " + self.last_name)
