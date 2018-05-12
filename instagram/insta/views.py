from django.shortcuts import render
from django.http  import HttpResponse
from .models import Post

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def profile(request):
    return render(request, 'profile.html')

def all_images(request):
    images = Post.get_posts()
    return render(request, 'all_images.html', {"images": images})
