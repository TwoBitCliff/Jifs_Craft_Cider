from django.shortcuts import render
from .models import Post


def PostList(request):
    """ A view to display blog posts """

    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)
