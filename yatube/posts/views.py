from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context) 


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context) 


def group_list(request, slug):
    template = 'posts/group_list.html'
    content = ("Здесь будет информация о группах проекта Yatube", slug)
    context = {
        'content': content,
    }
    return render(request, template, context)
