from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post
from django.contrib import admin
# from polls.models import Choice, Question


admin.site.register(Post)  # Importing the post model (from models.py defined before)

