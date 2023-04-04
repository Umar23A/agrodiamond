from django.urls import path

from pages.views import main_index, post, cat

urlpatterns = [
    path('', main_index, name='home'),
    path('post/<int:pk>/', post, name='post'),
    path('cat/', cat, name='cat')
]