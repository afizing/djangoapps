from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
import datetime

from .models import Question

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


def create_question(question_text, days):
  time = timezone.now() + timezone.timedelta(days=days)
  return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionViewTests(TestCase):
  def test_index_view_with_no_questions(self):
    response = self.client.get(reverse('polls:index'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "No polls are available.")
    self.assertQuerysetEqual(response.context['latest_question_list'], [])

  def test_index_view_with_a_past_questions(self):
    create_question(question_text="Past question.", days=-30)
    response = self.client.get(reverse('polls:index'))
    self.assertQuerysetEqual(response.context['latest_question_list'],
    ['<Question: Past question.>'])


class QuestionIndexDetailTests(TestCase):
  def test_detail_view_with_a_future_question(self):
    future_question = create_question(question_text='Future question.', days=5)
    url = reverse('polls:detail', args=(future_question.id,))
    response = self.client.get(url)
    self.assertEqual(response.status_code, 404)

