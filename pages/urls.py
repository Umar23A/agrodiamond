from django.urls import path

from pages.views import main_index, post,service_view

urlpatterns = [
    path('', main_index, name='home'),
    path('post/<int:pk>/', post, name='post'),
    path('service/', service_view, name='service')
]