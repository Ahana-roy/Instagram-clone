from django.contrib.auth.models import User
from comment.models import Comment
from django import forms


# Posting A comment 

class NewCommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'input form-control', 'placeholder': 'Write comment', 'rows': 3}), required=True)
    
    class Meta:
        model = Comment
        fields = ("body",)