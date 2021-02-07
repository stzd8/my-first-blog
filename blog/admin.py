from django.contrib import admin
from .models import Post

# Make Post model visible to admin page
admin.site.register(Post)


