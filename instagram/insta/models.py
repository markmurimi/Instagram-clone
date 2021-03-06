from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User


# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    
    def __str__(self):
        return self.first_name

    def save_editor(self):
        '''Method to save an editor in the database'''
        self.save()

    def delete_editor(self):
        ''' Method to delete an editor from the database'''
        self.delete()


class Post(models.Model):
    post_name = models.CharField(max_length = 30)
    post = models.ImageField(upload_to='posts/')
    post_caption = models.TextField()
    profile = models.ForeignKey('Profile')
    username = models.CharField(max_length =30, unique = True)
    photo_id = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    
    def __str__(self):
        return self.post_name

    def save_image(self):
        '''Method to save an image in the database'''
        self.save()

    def delete_image(self):
        ''' Method to delete an image from the database'''
        self.delete()

    @classmethod
    def get_posts(cls):
        '''
        Method that gets all image posts from the database
        Returns:
            get_posts : list of image post objects from the database
        ''' 
        images = Post.objects.all()
        return images

    @classmethod
    def search_by_username(cls,search_term):
        images = cls.objects.filter(username__icontains=search_term)
        return images

    @classmethod
    def get_image(cls, photo_id):
        '''
        Method that loopps through the class and pick an anticipated id
        Returns:
            selected_image : desired image
        '''
        selected_image = Post.objects.filter_by(id=photo_id)
        return selected_image

class Profile(models.Model):
    username = models.CharField(max_length =30, unique= True)
    profile_pic = models.ImageField(upload_to='profiles/')
    bio = models.TextField()
    profile_id = models.CharField(max_length = 30)
    picture = models.ImageField(upload_to= 'profiles/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

    def save_profile(self):
        '''Method to save the profile in the database'''
        self.save()

    def delete_profile(self):
        ''' Method to delete a profile from the database'''
        self.delete()

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()


class Comment(models.Model):
    '''
    Class that defines a Comment on a Post
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

    @classmethod
    def get_post_comments(cls, post_id):
        ''' Function that gets all the comments belonging to a single post
        Args:
            post_id : specific post
        Returns:
            comments : List of Comment objects for the specified post
        '''
        comments_list = Comment.objects.filter(post=post_id)

        return comments_list