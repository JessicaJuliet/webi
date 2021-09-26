from django.shortcuts import render, get_object_or_404
from .models import Blog


def blog(request):
    """ A function to render the Blog page """

    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blog.html', context)


def blog_post(request, slug):
    """ A function to render individual blog post pages """

    blog = get_object_or_404(Blog, slug=slug)
    context = {
        'blog': blog,
    }
    
    return render(request, 'blog/blog_post.html', context)
