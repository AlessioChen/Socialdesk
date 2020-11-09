from django.db import models  #models Master class
from django.utils import timezone
from django.contrib.auth.models import User #default Django User table
from .utils import sendTransaction
import hashlib


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if a user is deleted also the post is deleted
    hash = models.CharField(max_length=32, default= None, null = True)
    txId = models.CharField(max_length=66, default=None, null = True)

    # This method writes the content message in the Ropsten Ethereum 
    def write_on_chain(self):
        self.hash = hashlib.sha256(self.content.encode('utf-8')).hexdigest()
        self.txId = sendTransaction(self.hash)
        self.save()


    def __str__(self):
        return self.title 