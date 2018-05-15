from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Post,Profile
from .forms import NewsLetterForm, NewPostForm, ProfileForm, ImagePostForm
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

def profile(request, profile_id):
    profile = Profile.objects.get(profile_id = profile_id)
    return render(request, 'profile.html', {"profile":profile})

def all_images(request):
    images = Post.get_posts()
    return render(request, 'all_images.html', {"images": images})



def home(request):
    return render(request, "registration/home.html")

def image_details(request, photo_id):
    photo = Post.objects.filter_by(id=photo_id)
    return render(request, 'details.html', {'photo': photo})


def post(request,photo_id):
    try:
        post = Post.objects.get(id = photo_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all_images.html", {"post":post})

def search(request):

    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_post = Post.search_by_username(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"posts": searched_post})

    else:
        message = "You haven't searche/d for any term"
        return render(request, 'search.html',{"message":message})

def follow(request, profile_id):
    profile = Profile.objects.get(profile_id = profile_id)
    return render(request, 'follower.html', {"profile":profile})

def explore(request):
    images = Post.get_posts()
    return render(request, 'explore.html', {"images":images})

@login_required(login_url='/accounts/login')
def create_profile(request):
    '''
    View function to create and update the profile of the user
    '''
    current_user = request.user

    profiles = Profile.objects.filter(user=current_user).count()

    if request.method == 'POST':

        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid:

            if profiles == 0:
                k = form.save(commit=False)
                k.user = current_user
                k.save()
                return redirect(profile)
            else:
                record = Profile.objects.filter(user=current_user)
                record.delete()
                k = form.save(commit=False)
                k.user = current_user
                k.save()
                return redirect(profile)
    else:
        form = ProfileForm()
    return render(request, 'update-profile.html', {"form": form})

@login_required(login_url='/accounts/login')
def new_post(request):
    '''
    View function to display a form for creating a post to a logged in authenticated user
    '''
    current_user = request.user

    if request.method == 'POST':

        form = ImagePostForm(request.POST, request.FILES)

        if form.is_valid:
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect(profile)
    else:
        form = ImagePostForm()
    return render(request, 'new-post.html', {"form": form})