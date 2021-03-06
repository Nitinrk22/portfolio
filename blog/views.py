from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Blog


def allblog(request):
    blogs = Blog.objects
    return render(request, 'blog/allblog.html', {'blogs':blogs})


def detail(request, blogid):
    detailblog = get_object_or_404(Blog, pk=blogid)
    return render(request, 'blog/detail.html', {'blog':detailblog})
