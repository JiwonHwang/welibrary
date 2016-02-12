from django import forms
from django.core.mail import send_mail

from .models import Post, Contact

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'author',  'postcategory', 'content')


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')
