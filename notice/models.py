from __future__ import unicode_literals
from user_manage.models import User
from django.db import models

# Create your models here.

class Bulletin(models.Model):
    creator = models.ForeignKey(User, related_name='created_bulletin')
    follower = models.ManyToManyField(User , related_name='bulletin_follower')
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255, default='This is a bulletin description.')

    def __unicode__(self):
        return self.name

class Notice(models.Model):
    author = models.ForeignKey(User, related_name='article_author')
    bulletin = models.ForeignKey(Bulletin, related_name='bulletin')
    title = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=255)

    class Meta:
        ordering = ['-date_created']

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    belong_to = models.ForeignKey(Notice, related_name='comment_belong_to')
    subject = models.CharField(max_length=30)
    author = models.ForeignKey(User)
    content = models.TextField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __unicode__(self):
        return self.subject
