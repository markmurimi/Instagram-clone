from django import forms
from .models import Post,Profile, Comment

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class NewPostForm(forms.ModelForm):
    post_name = forms.CharField(label='Post Name', max_length = 30)
    post = forms.ImageField(label='Image')
    username = forms.CharField( label='Username', max_length =30, )
    model = Post

class ProfileForm(forms.ModelForm):
    '''
    classs that creates profile update form
    '''
    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio', 'user', 'profile_id']

class ImagePostForm(forms.ModelForm):
    '''
    Class to create a form for an authenticated user to create Post
    '''
    class Meta:
        model = Post
        fields = ['post', 'post_name', 'post_caption', 'username', 'profile']

class CommentForm(forms.ModelForm):
    '''
    class that creates the comment form
    '''
    class Meta:
        model = Comment
        fields = ['comment']