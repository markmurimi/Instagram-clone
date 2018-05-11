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

    # Testing Save Method
    def test_save_method(self):
        self.mark.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)