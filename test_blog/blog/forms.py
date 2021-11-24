from django import forms
from .models import Post


class PostUpdateForm(forms.Form):

    class Meta():
        Model = Post
        fields = ['title', 'content', 'post_image']