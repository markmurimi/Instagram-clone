from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Post
from .forms import NewsLetterForm, NewPostForm
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.current_user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.editor = current_user
            post.save()
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form":form})

def home(request):
    return render(request, "registration/home.html")

def image_details(request, photo_id):
    photo = Post.objects.get(id=photo_id)
    return render(request, 'details.html', {'photo': photo})


def post(request,photo_id):
    try:
        post = Post.objects.get(id = photo_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all_images.html", {"post":post})

def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_post = Post.search_by_username(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"posts": searched_post})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})