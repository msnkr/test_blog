from django.shortcuts import render
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


class PostUpdateView(UpdateView):
    pass


class PostCreateView(CreateView):
    pass


class PostDeleteView(DeleteView):
    pass





