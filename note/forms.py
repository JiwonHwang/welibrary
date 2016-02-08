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


# class ContactForm(fomrs.Form):
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea)
#     sender = forms.EmailField()
#     cc_myself = forms.BooleanField(requred=False)

#     if form.is_valid():
#         subject = form.cleaned_data['subject']
#         message = form.cleaned_data['message']
#         sender = form.cleaned_data['sender']
#         cc_myself = form.cleaned_data['cc_myself']

#         recipients = ['rhasu2003@gmail.com']
#         if cc_myself:
#             recipients.append(sender)

#         send_mail(subject, message, sender, recipients)
#         return HttpResponseRedirect('/thanks/')
#         # 이 위에 줄 ?? HttpResponseRedirect 를 library에서 가져와야 하는지? 'thanks'링크는 어디로 넣어줘야 하는지? 만들어줘야 하는지 체크