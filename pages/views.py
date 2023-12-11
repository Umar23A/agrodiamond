from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Category, Post, Service
from django.utils.translation import gettext as _


def main_index(request):
    request.page_title = _("Bosh sahifa")
    categories = Category.objects.all()
    return render(request, 'index.html',{
        'categories': categories
    })


def post(request, pk):
    request.page_title = _("Bizning Mahsulotlar")
    post = Post.objects.filter(category_id=pk)

    return render(request, 'post.html', {
        'post': post
    })


def service_view(request):
    request.page_title = _("Bizning xizmatlar")
    services = Service.objects.all()
    return render(request, 'service.html',{
        'services': services
    })



