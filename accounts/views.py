from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserCreateForm
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages


def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            login(request, user)
            messages.add_message(request, messages.INFO,
                'Thank you for registering! 등록해주셔서 감사합니다! :D',
                'message register-success')
            return HttpResponseRedirect('/')
    else:
        form = UserCreateForm()
    return render(request, 'registration/register.html', { 'form': form })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


