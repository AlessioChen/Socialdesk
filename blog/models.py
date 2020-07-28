from django.db import models  #models Master class
from django.utils import timezone
from django.contrib.auth.models import User #default Django User table


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if a user is deleted also the post is deleted
    
