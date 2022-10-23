from django.shortcuts import get_object_or_404, render

from .models import post

def detail(request, slug):
    Post = get_object_or_404(post, slug=slug )

    return render(request, 'blog/detail.html', {'post': Post})
