from django.forms import fields, forms, widgets
from .models import Post

class PostCreateForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = 'content'

        widgets = {
            
        }
   
