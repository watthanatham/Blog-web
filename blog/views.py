# import django class
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse

# import models
from .models import Post

# Create your views here.
def index(request):
  posts = Post.objects.filter(status=True)
  
  paginator = Paginator(posts, 3)
  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  
  return render(request, 'index.html', {'page_obj': page_obj})
  

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