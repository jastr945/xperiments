from django.test import TestCase
from searchapp.models import Article
from django.test import Client
from django.urls import reverse
from django.core.urlresolvers import reverse


client = Client()

class ArticleViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        article = Article.objects.create(title='Django', slug='django', date='2017-09-25', category="django")

    def test_category_url(self):
        article = Article.objects.get(title="Django")
        resp = self.client.get('index', kwargs={'category': article.category})
        self.assertEqual(resp.status_code, 200)

    def test_article_url(self):
        article = Article.objects.get(title="Django")
        resp = self.client.get(reverse('article', args=(article.slug,)))
        self.assertEqual(resp.status_code, 200)

    def test_start_url(self):
        resp = self.client.get(reverse('start'))
        self.assertEqual(resp.status_code, 200)

    def test_index_url(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.context['articles']), 1)

    def test_search_url(self):
        resp = self.client.get(reverse('search'))
        self.assertEqual(resp.status_code, 200)
