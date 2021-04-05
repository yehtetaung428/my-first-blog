from django import forms

from .models import Post, Comment

# form for Post model
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

# form for Comment model
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)