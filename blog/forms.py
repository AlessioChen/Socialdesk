from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    # classe con cui diciamo a Django quale model utilizzare per creare questo form
    class Meta:
        model = Post
        fields = ('title', 'content',)
