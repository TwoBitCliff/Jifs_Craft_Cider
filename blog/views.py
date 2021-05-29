from django.shortcuts import render, redirect, reverse
from .models import Post
from .forms import NewPostForm
from django.contrib import messages


def PostList(request):
    """ A view to display blog posts """

    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)


def CreateNewPost(request):
    """  Adds a post to the blog  """
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog post added!')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
    else:
        form = NewPostForm()
    template = 'blog/new-post.html'
    context = {
        'form': form
    }

    return render(request, template, context)
