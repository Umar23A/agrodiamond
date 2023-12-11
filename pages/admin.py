from django.contrib import admin
from .models import Category, Post, Service

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Service)