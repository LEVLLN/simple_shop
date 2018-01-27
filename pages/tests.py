from django.test import TestCase
from django.test import SimpleTestCase
from .models import Content
from django.urls import reverse
# Create your tests here.
# pages/tests.py



class ContentModelTest(TestCase):
    """docstring for ContentModelTest"""
    @classmethod
    def setUpTestData(cls):
       Content.objects.create(text="The test data")

    def test_text_content(self):
        content = Content.objects.get(id=1)
        expected_object_name = f'{content.text}'
        self.assertEquals(expected_object_name, 'The test data')

class HomePageViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Content.objects.create(text='this is another test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEquals(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEquals(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')

class AboutPageViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Content.objects.create(text='this is another test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/about/')
        self.assertEquals(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('about'))
        self.assertEquals(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('about'))
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'about.html')