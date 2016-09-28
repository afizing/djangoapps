from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
  posts = Post.objects.all()
  context = {
  'posts':posts
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
  context = {
    'form':form
  }
  return render(request, 'blog/create.html', context)


def hello(request):
  return HttpResponse("Hello World!!")


