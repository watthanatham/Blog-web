from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
  posts = Post.objects.filter(status=True)
  return render(request, 'index.html', {'posts': posts})

def post_detail(request, id):
  post = Post.objects.get(id=id, status=True)
  return render(request, 'post_detail.html', {'post': post})

def post_search(request):
  if 'search_keyword' in request.GET:
    search_keyword = request.GET['search_keyword']
    posts = Post.objects.filter(title__contains = search_keyword, status=True)
    return render(request, 'index.html', {'posts': posts})
  else:
    return redirect('index')