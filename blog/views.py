from django.shortcuts import render
from .models import Blog


def blog(request):
    """ A view to return the blog page """
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/blog.html', context)
