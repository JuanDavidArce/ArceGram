"""post forms"""
#Django
from django import forms
from django.forms import fields

#Models
from posts.models import Post

class PostForm(forms.ModelForm):
    """Post model form"""
    class Meta:
        """Form settings"""
        model=Post
        fields={'user','profile','title','photo'}