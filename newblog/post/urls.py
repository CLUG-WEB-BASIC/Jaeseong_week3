from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.read_blog_list, name='read_blog_list'),
]