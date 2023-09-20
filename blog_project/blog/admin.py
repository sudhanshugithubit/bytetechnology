from django.contrib import admin

# Register your models here.
from .models import Post  # Replace '.models' with the correct import path to your 'Post' model.

admin.site.register(Post)
