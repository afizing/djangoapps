from django.test import TestCase
from django.utils import timezone
import datetime

from .models import Question
from .views
# Create your tests here.

class QuestionMethodTests(TestCase):

  def test_was_published_recently_with_future_question(self):
    time = timezone.now() + datetime.timedelta(days=30)
    f_question = Question(pub_date=time)
    self.assertEqual(f_question.was_published_recently(), False)

  def test_was_published_recently_with_recent_question(self):
    time = timezone.now()
    f_question = Question(pub_date=time)
    self.assertEqual(f_question.was_published_recently(), True)

  def test_was_published_recently_with_old_question(self):
    time = timezone.now()- datetime.timedelta(days=30)
    f_question = Question(pub_date=time)
    self.assertEqual(f_question.was_published_recently(), False)
