from django.contrib import admin
from .models import Post, Comment

# Register your models here.

# Post model by admin
admin.site.register(Post)

# comment model by admin
admin.site.register(Comment)