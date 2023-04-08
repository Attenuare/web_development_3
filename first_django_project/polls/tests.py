from django.test import TestCase

class HomeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/polls/')

    def test_200_response(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_text(self):
        self.assertContains(self.resp, 'Welcome!')

    def test_templates_home(self):
        self.assertTemplateUsed(self.resp, 'home.html')

class ChristmasTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/polls/christmas')

    def test_200_response(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_text(self):
        self.assertContains(self.resp, 'Christmas')

    def test_templates_christmas(self):
        self.assertTemplateUsed(self.resp, 'christmas.html')

class TiradentesTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/polls/tiradentes')

    def test_200_response(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_text(self):
        self.assertContains(self.resp, 'Tiradentes')

    def test_templates_tiradentes(self):
        self.assertTemplateUsed(self.resp, 'tiradentes.html')