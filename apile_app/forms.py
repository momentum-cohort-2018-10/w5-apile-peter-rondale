from django import forms
from apile_app.models import Post
from apile_app.models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('description',)
