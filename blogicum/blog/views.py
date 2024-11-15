from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now

from .models import Post
from .models import Category
# from .models import Location
# from .models import User


def index(request):
    post_list = Post.objects.select_related(
        'category',
        'location',
        'author'
    ).filter(
        pub_date__lte=now(),
        is_published=True,
        category__is_published=True
    ).order_by('pub_date')[0:5]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    post = get_object_or_404(
        Post,
        pk=id,
        pub_date__lte=now(),
        is_published=True,
        category__is_published=True,
    )
    post = Post.objects.select_related(
        'category',
        'location',
        'author'
    ).filter(pk=id)[0]
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category, slug=category_slug, is_published=True
    )
    post_list = Post.objects.select_related(
        'category',
        'location',
        'author'
    ).filter(
        pub_date__lte=now(),
        is_published=True,
        category__slug=category_slug
    )
    context = {
        'post_list': post_list,
        'category': category,
    }
    return render(request, 'blog/category.html', context)
