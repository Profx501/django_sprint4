from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Post, Category
from django.utils import timezone


def index(request):
    template_name = 'blog/index.html'
    post_list = Post.objects.select_related(
        'author',
        'location',
        'category'
    ).filter(
        pub_date__lt=timezone.now(),
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:5]
    context = {
        'post_list': post_list,
    }
    return render(request, template_name, context)


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.select_related(
            'author',
            'location',
            'category'
        ).filter(
            pub_date__lt=timezone.now(),
            is_published=True,
            category__is_published=True
        ), pk=post_id
    )
    template_name = 'blog/detail.html'
    context = {
        'post': post
    }
    return render(request, template_name, context)


def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    post_list = get_list_or_404(
        category.posts.filter(
            is_published=True,
            pub_date__lt=timezone.now(),
            category__is_published=True
        )
    )
    template_name = 'blog/category.html'
    context = {
        'post_list': post_list,
        'category': category
    }
    return render(request, template_name, context)
