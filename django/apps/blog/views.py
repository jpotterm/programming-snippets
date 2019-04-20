from django.shortcuts import get_object_or_404, redirect, render
from dwaiter.django.utils import paginate

from . import models


def listing(request):
    posts = models.Post.objects.published(for_user=request.user)

    # Categories

    active_category = None
    active_category_pk = request.GET.get('category', '')

    if active_category_pk != '':
        active_category = get_object_or_404(models.Category, pk=active_category_pk)
        posts = posts.filter(category=active_category)

    # Pagination
    posts = paginate(posts, request.GET.get('page', 1), 20)

    context = {
        'page': models.BlogListingPage.get_solo(),
        'categories': models.Category.objects.all(),
        'active_category': active_category,
        'posts': posts,
    }

    return render(request, 'apps_blog/listing.html', context)


def detail(request, pk, slug):
    post = get_object_or_404(models.Post.objects.published(for_user=request.user), pk=pk)

    if slug != post.get_slug():
        return redirect(post, permanent=True)

    context = {
        'post': post,
    }

    return render(request, 'apps_blog/detail.html', context)
