from django import forms
from apile_app.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description',)
