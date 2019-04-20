from django.shortcuts import get_object_or_404, redirect, render

from . import models


def detail(request, pk, slug):
    post = get_object_or_404(models.Post, pk=int(pk))

    if slug != post.get_slug():
        return redirect(post, permanent=True)

    context = {
        'one': 1,
    }

    return render(request, 'detail.html', context)
