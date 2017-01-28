from unidecode import unidecode

from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

from taggit.managers import TaggableManager
from mptt.models import MPTTModel, TreeForeignKey


class Post(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, max_length=250)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    tags = TaggableManager(blank=True)
    image = models.ImageField(upload_to="images/%Y/%m/", blank=True, null=True)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True, related_name="type")

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug, })

    # create slug
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(unidecode(self.title))
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, max_length=250)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(unidecode(self.name))
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

class Author(models.Model):
    username = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    about = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='images/user/', blank=True, null=True, default='images/default-avatar.jpg')

    def __str__(self):
        return str(self.first_name + " " + self.last_name)


class Comment(MPTTModel):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, null=True, related_name='comments')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='replies', db_index=True)

    name = models.CharField("Imię lub nick", max_length=250)
    email = models.EmailField("Adres e-mail", max_length=250, blank=True, null=True)
    website = models.CharField("Strona WWW", max_length=250, blank=True, null=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    content = models.TextField("Treść")

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)

    def __str__(self):
        return str("{}: {}...".format(self.name, self.content[:50]))
