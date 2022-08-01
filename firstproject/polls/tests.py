import datetime

from django.test import TestCase
from django.urls.base import reverse
from django.utils import timezone

from .models import Question

# Lo más común es hacer tests sobre modelos y/o vistas en Django

class QuestionModelTests(TestCase): #Bateria de test para el modelo Question que fue importado 

    def test_was_published_recently_with_future_questions(self):
        """was_published_recently returns False for questions whose pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(
        question_text="¿Quién es el mejor Course Director de Platzi?", pub_date=time)
        self.assertIs(future_question.was_published_recently, False)

class QuestionIndexViewTests(QuestionModelTests, TestCase):
    def test_no_questions(self):
        """If no question exist, an appropiate message is displayed"""
        response = self.client.get(reverse('polls:index')) #Hago una petición GET al index de polls y guardo la respuesta en response
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_show_only_recent_questions(self):
        """The view should only show recent questions. It cannot show future questions from the date they are consulted."""
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        future_question = [self.question, self.future_time]
        self.assertNotContains(response, future_question)


