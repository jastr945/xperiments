from django.test import TestCase
from .models import Article
from django.test.utils import setup_test_environment
from django.test import Client
from django.urls import reverse


# setup_test_environment()
client = Client()


class ArticleTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)


class ArticleViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Create 13 authors for pagination tests
        number_of_articles = 2
        for article_num in range(number_of_articles):
            Article.objects.create(title='{}'.format(article_num), body='{}'.format(article_num), date='2017-09-25')

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('index1'))
        self.assertEqual(resp.status_code, 200)
