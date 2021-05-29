from django import forms
from .models import Post

# https://www.youtube.com/watch?v=PJkV76KTZqk


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'title', 'content')

        