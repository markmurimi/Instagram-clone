from django.test import TestCase
from .models import Editor,Post
# Create your tests here.

class EdtitorTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.mark= Editor(username = '_illest.niccur',editor_name = 'mark', email = 'murimimg180@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.mark,Editor))