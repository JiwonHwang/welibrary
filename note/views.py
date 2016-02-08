from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PostForm, ContactForm

from .models import Post, Contact


# main page
def index(request):
    return render(request, 'note/index.html', {})


def about(request):
    return render(request, 'note/about.html', {})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'note/post_list.html', {'post_list': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'note/post_detail.html', {
        'post': post
        })

# post_new , post_eidt 은 아직  site에서 사용하지 않아도 됨. 새로운 Post는 일단 admin에서 추가하기
def post_new(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.published_date=timezone.now()
            post.save()
            return redirect('/note/post_list.html', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'note/post_new.html', {'post_form': post_form})

#==================================================

def new_contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if form.is_valid():
            contact=form.save(commit=False)
            contact.save()
            return render(request, 'note/contact.html', {'contact_form': contact_form})
    else:
        contact_form = PostForm()
    return render(request, 'note/contact.html', {'contact_form': contact_form})

#===================

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method=="POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            # post.author=request.user
            post.published_date=timezone.now()
            post.save()
            return redirect('note.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'note/post_edit.html', {'form': form})


# ------ python, Django, Frontend 리스트 & detail views -----
def python_list(request):
    python_posts = Post.objects.filter(postcategory="python").filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'note/python_list.html', {'python_posts': python_posts})


def python_detail(request, pk):
    python_post = get_object_or_404(Post, pk=pk)
    return render(request, 'note/python_detail.html', {
        'python_post': python_post
        })

#----------------------------------------------------

def django_list(request):
    django_posts = Post.objects.filter(postcategory="django").filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'note/django_list.html', {'django_posts': django_posts})


def django_detail(request, pk):
    django_post = get_object_or_404(Post, pk=pk)
    return render(request, 'note/django_detail.html', {
        'django_post': django_post
        })

#----------------------------------------------------

def frontend_list(request):
    frontend_posts = Post.objects.filter(postcategory="frontend").filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'note/frontend_list.html', {'frontend_posts': frontend_posts})


def frontend_detail(request, pk):
    frontend_post = get_object_or_404(Post, pk=pk)
    return render(request, 'note/frontend_detail.html', {
        'frontend_post' : frontend_post
        })
# ------


# [   ] def contact
# [  O ] 1.  models.py - class Contact
# [  O ] 2.  forms.py - make form for contact
# [  O? ] 3. add contact form at views.py
# [   ] 4. check the link at urls.py


