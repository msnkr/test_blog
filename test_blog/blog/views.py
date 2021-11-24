from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    ordering = ['-date_published']
    paginate = 5


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    login_url = '/login/'
    redirect_field_name = 'post_create'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'author']

    login_url = '/login/'
    redirect_field_name = 'post_create'


# class PostDeleteView(DeleteView):
#     pass





