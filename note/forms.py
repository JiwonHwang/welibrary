from django import forms
from django.core.mail import send_mail

from .models import Post, Contact, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'author',  'postcategory', 'content')


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)