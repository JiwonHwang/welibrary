from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PostForm, ContactForm, CommentForm
from django.contrib.auth.decorators import login_required
from .models import Post, Contact, Comment


# main page
def index(request):
    return render(request, 'note/index.html', {})


def about(request):
    return render(request, 'note/about.html', {})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'note/post/post_list.html', {'post_list': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'note/post/post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form= PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('note.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'note/post/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method=="POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author=request.user
            post.published_date=timezone.now()
            post.save()
            return redirect('note.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'note/post/post_edit.html', {'form': form})


@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'note/post/post_draft_list.html', {'posts': posts})


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('note.views.post_detail', pk=pk)


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('note.views.post_list')


# ------ python, Django, Frontend : list, detail, add_comment_to_post -----
def python_list(request):
    python_posts = Post.objects.filter(postcategory="python").filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'note/python/python_list.html', {'python_posts': python_posts})


def python_detail(request, pk):
    python_post = get_object_or_404(Post, pk=pk)
    return render(request, 'note/python/python_detail.html', {'python_post': python_post})


def python_add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('note.views.python_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'note/python/python_add_comment_to_post.html', {'form': form})


@login_required
def python_comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('note.views.python_detail', pk=comment.post.pk)


@login_required
def python_comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('note.views.python_detail', pk=post_pk)


#----------------------------------------------------

def django_list(request):
    print('sdfghjkhgfdfghjjhgfddfghjkjhgfdsdfghj')
    django_posts = Post.objects.filter(postcategory="django").filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'note/django/django_list.html', {'django_posts': django_posts})


def django_detail(request, pk):
    django_post = get_object_or_404(Post, pk=pk)
    return render(request, 'note/django/django_detail.html', {'django_post': django_post})

#----------------------------------------------------

def frontend_list(request):
    frontend_posts = Post.objects.filter(postcategory="frontend").filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'note/frontend/frontend_list.html', {'frontend_posts': frontend_posts})


def frontend_detail(request, pk):
    frontend_post = get_object_or_404(Post, pk=pk)
    return render(request, 'note/frontend/frontend_detail.html', {'frontend_post' : frontend_post})

#------------------------------------------------------

def contact_new(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact=contact_form.save(commit=False)
            contact.save()
            return render(request, 'note/contact/contact_result.html', {'contact_form': contact_form})
            #여기서는 'Thank you'나 'Success' 화면을 보여줘야 할 거 같은데?
    else:
        contact_form = ContactForm() # 이 부분을 PostForm으로 해두어서 계속 PostForm이 contact_new.html에 나타났던 것.
    return render(request, 'note/contact/contact_edit.html', {'contact_form': contact_form})

#-----------------------------------------

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('note.views.post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'note/post/add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('note.views.post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pkcomment.delete()
    return redirect('note.views.post_detail', pk=post_pk)

