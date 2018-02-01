from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    Post = models.CharField(max_length=500)
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now=True)