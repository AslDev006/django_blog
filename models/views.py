from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def HomePageView(request):
    last_post = Post_Model.published.all().order_by('-publish_time')[:1]
    first_last_posts = Post_Model.published.all().order_by('-publish_time')[1:4]
    second_last_posts = Post_Model.published.all().order_by('-publish_time')[4:7]
    context = {
        "last_post": last_post,
        "first_last_posts": first_last_posts,
        "second_last_posts": second_last_posts,
    }
    return render(request, 'Pages/index.html', context)

def AboutPageView(request):
    return render(request, 'Pages/about.html', {})

def BlogPageView(request):
    posts = Post_Model.published.all().order_by('-publish_time')
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 1)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)

    context = {
        "pages": pages,
    }
    return render(request, 'Pages/blog.html', context)

def ContactPageView(request):
    return render(request, 'Pages/contact.html', {})


def SinglePageView(request, slug):
    post = get_object_or_404(Post_Model, slug=slug, status=Post_Model.Status.Published)

    context = {
        "post": post,
    }
    return render(request, 'Pages/single.html', context)
