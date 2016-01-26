from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PostForm
from .models import Post



def index(request):
    return render(request, 'note/index.html', {})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'note/post_list.html', {'post_list': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'note/post_detail.html', {'post': post })


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.published_date=timezone.now()
            post.save()
            return redirect('note.views.post_detail', pk=post.pk)


    else:
        form = PostForm()
    return render(request, 'note/post_detail.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method=="POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post.author=request.user
            post.published_date=timezone.now()
            post.save()
            return redirect('note.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'note/post_edit.html', {'form': form})