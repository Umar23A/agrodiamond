from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Category, Post

def main_index(request):
    categories = Category.objects.all()
    return render(request, 'index.html',{
        'categories': categories
    })


def post(request, pk):
    post = Post.objects.filter(category_id=pk)

    return render(request, 'post.html', {
        'post': post
    })

def cat(request):
    return render(request, 'cat.html')



