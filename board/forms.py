from django import forms
from .models import Comment, Thread

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'comment_text',)

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ('thread_title', 'thread_text',)