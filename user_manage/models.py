from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class User(User):
    security_question = models.CharField(max_length=256, default='')
    security_answer = models.CharField(max_length=256, default='')
    avatar = models.CharField(max_length=256, default='/img/icon.png')
    def __unicode__(self):
        return self.username

