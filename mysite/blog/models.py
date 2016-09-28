from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse



# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=50)
  content= models.TextField(max_length=5000)
  timestamp = models.DateField(auto_now=False, auto_now_add=True)
  updated= models.DateField(auto_now=True, auto_now_add=False)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse("blog:detail", kwargs={'post_id': self.id})

