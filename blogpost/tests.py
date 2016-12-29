from django.test import TestCase, LiveServerTestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from selenium import webdriver

from blogpost.views import index, view_post
from blogpost.models import Blogpost
from datetime import datetime


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        self.assertIn(b'<title>Welcome To My Blog</title>', response.content)

class BlogpostTest(TestCase):
    def test_blogpost_url_resolves_to_blog_post_view(self):
        found = resolve('/blog/this_is_a_test.html')
        self.assertEqual(found.func, view_post)

    def test_blogpost_create_with_view(self):
        Blogpost.objects.create(title='hello', author='admin', slug='this_is_a_test', body='This is a blog',
                                posted=datetime.now)
        response = self.client.get('/blog/this_is_a_test.html')
        self.assertIn(b'This is a blog', response.content)

class HomePageTestCase(LiveServerTestCase):
    def setUp(self):
        chromedriver = 'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver'
        self.selenium = webdriver.Chrome(executable_path=chromedriver)
        self.selenium.maximize_window()
        super(HomePageTestCase, self).setUp()
    def tearDown(self):
        self.selenium.quit()
        super(HomePageTestCase, self).tearDown()

    def test_visit_homepage(self):
        self.selenium.get(
            '%s%s' % (self.live_server_url, "/")
        )
        self.assertIn("Welcome To My Blog", self.selenium.title)
