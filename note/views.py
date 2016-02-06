from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PostForm

from .models import Post


# main page
def index(request):
    return render(request, 'note/index.html', {})


def about(request):
    return render(request, 'note/about.html', {})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'note/post_list.html', {'post_list': posts})

# ------ python, Django, Frontend 리스트 -----
def python_list(request):
    python_posts = PythonPosts.objects.filter(postcategory="Python").filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'note/python_list.html', { 'python_list': python_posts})


def django_list(request):
    django_posts = DjangoPosts.objects.filter(postcategory="Django").filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'note/django_list', {'django_list': django_posts})


def frontend_list(request):
    frontend_posts = FrontendPosts.objects.filter(postcategory="Frontend").filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'note/frontend_list', {'frontend_list': frontend_posts})

# ------



def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'note/post_detail.html', {
        'post': post
        })


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            # post.author=request.user
            post.published_date=timezone.now()
            post.save()
            return redirect('/note/post/list/', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'note/post_new.html', {'form': form})


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


# [   ] def contact
# 1.  models.py - class Contact
# 2.  forms.py - make form for contact
# 3. add contact form at views.py
# 4. check the link at urls.py


