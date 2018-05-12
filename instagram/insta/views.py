from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Post
from .forms import NewsLetterForm
from django.contrib.auth.decorators import login_required.

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('welcome')  
    else:
        form = NewsLetterForm()
    return render(request,'welcome.html',{"letterForm":form})

def profile(request):
    return render(request, 'profile.html')

def all_images(request):
    images = Post.get_posts()
    return render(request, 'all_images.html', {"images": images})
