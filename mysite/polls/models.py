from __future__ import unicode_literals
from django.utils import timezone
from django.core.urlresolvers import reverse
import datetime

from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
      now = timezone.now()
      return now >= self.pub_date >= now-datetime.timedelta(days=1)
    def get_absolute_url(self):
      # return "/polls/%i/"%self.id
      return reverse('polls.views.DetailView.as_view()', args=[self.id])


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models . CASCADE )
    choice_text = models.CharField( max_length = 200 )
    votes = models.IntegerField( default = 0 )
    def __str__(self):
        return self.choice_text

