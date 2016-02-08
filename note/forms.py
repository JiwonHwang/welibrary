from django import forms

from .models import Post, Contact

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'author',  'postcategory', 'content')


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')