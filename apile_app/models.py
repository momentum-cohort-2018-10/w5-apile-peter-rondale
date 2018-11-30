from django.contrib.auth.models import User
from django.db import models
from slugify import slugify

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    date_added = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def save(self):
        if not self.id:
            self.slug = slugify(self.title)
        super(Post, self).save()

    def is_liked_by_user(self, author):
        """
        Get all of the votes for posts, filter by the logged in user, tell whether or not it has been liked
        """
        return self.posts.filter(author=user).count() > 0

# class Comment(models.Model):
#     author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, blank=True)
#     post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
#     description = models.TextField(null=True)
#     date_added = models.DateTimeField(auto_now=True)

class Vote(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, related_name='votes')

    class Meta:
        unique_together = (
            'post',
            'author',
        )
class Comment(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, blank=True)
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    date_added = models.DateTimeField(auto_now=True)
