from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
  posts = Post.objects.all().order_by('timestamp')
  context = {
  'posts':posts.reverse()
  }
  return render(request, 'blog/index.html', context)


def detail(request, post_id):
  post = get_object_or_404(Post, id=post_id)
  context = {
  'post':post
  }
  return render(request, 'blog/detail.html', context)


def create(request):
  form = PostForm(request.POST or None)
  if form.is_valid():
    instance = form.save(commit=False)
    instance.save()
    messages.success(request, "New post is created")
    return HttpResponseRedirect(instance.get_absolute_url())

  context = {
    'form':form
  }
  return render(request, 'blog/create.html', context)


def update(request, post_id=None):
  instance = get_object_or_404(Post, id=post_id)
  form = PostForm(request.POST or None, instance=instance)
  if form.is_valid():
    instance = form.save(commit=False)
    instance.save()
    messages.success(request, "Post Updated")
    return HttpResponseRedirect(instance.get_absolute_url())
    # redirect('blog:detail', id=post_id)
  return render(request, 'blog/update.html', {'form': form})


def delete(request, post_id=None):
  instance = get_object_or_404(Post, id=post_id)
  instance.delete()
  messages.success(request, "Post deleted")
  return redirect('blog:index')


def hello(request):
  return HttpResponse("Hello World!!")


