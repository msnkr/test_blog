from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'post_image, content')


