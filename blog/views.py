from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Post
from django.core.paginator import Paginator


# Create your views here.

class BlogPageView(ListView):
    model = Post
    template_name = "index.html"
    paginate_by = 2

class BlogDetailView(DetailView):
    model = Post
    template_name = "post.html"

def about(request):
   return render(request, 'about.html')





