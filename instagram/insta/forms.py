from django import forms
from .models import Post

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class NewPostForm(forms.ModelForm):
    post_name = forms.CharField(label='Post Name', max_length = 30)
    post = forms.ImageField(label='Image')
    username = forms.CharField( label='Username', max_length =30, )
    model = Post