from django import forms
from django.contrib.auth.forms import UserCreationForm
# https://github.com/django/django/blob/master/django/contrib/auth/forms.py
from django.contrib.auth.models import User


class UserCreateFrom(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        # Where does this 'User models comes from?
        #Check the source code in django github'
        # A. https://github.com/django/django/blob/master/django/contrib/auth/base_user.py
        fields = ("username", "email", "password1", "password2",
                    "first_name", "last_name")

    def save(self, commit=True):
        user = super(UserCreateFrom, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

