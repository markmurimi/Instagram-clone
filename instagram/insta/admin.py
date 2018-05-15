from django.contrib import admin
from .models import Comment, Editor,Post,Profile

# Register your models here.
admin.site.register(Editor)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Profile)