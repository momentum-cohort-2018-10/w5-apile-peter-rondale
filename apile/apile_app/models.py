from django.contrib.auth.models import User
from django.db import models
from slugify import slugify
#from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=255)
    #author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    date_added = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    #def save(self):
        #if not self.id:
            #self.slug = slugify(self.id)
        #super(Post, self).save()