from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Page

admin.site.register(Page)  # Importing the post model (from models.py defined before)
