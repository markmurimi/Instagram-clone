from django.db import models
from django import forms

# Create your models here.
class Post(models.Model):
    post_name = models.CharField(max_length =30)
    post_caption = models.TextField()
    editor = models.ForeignKey('Editor')
    post = models.ImageField()

class Editor(models.Model):
    username = models.CharField(max_length =10, unique=True)
    editor_name = models.CharField(max_length =30)
    email = models.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    profile_photo = models.ImageField()
    user_bio = models.TextField()

    def __str__(self):
        return self.editor_name
    