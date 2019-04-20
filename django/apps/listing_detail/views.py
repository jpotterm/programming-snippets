from django.shortcuts import get_object_or_404, redirect, render
from dwaiter.django.utils import paginate

from . import models


def listing(request):
    items = models.Item.objects.published(for_user=request.user)

    # Pagination
    items = paginate(posts, request.GET.get('page', 1), 20)

    context = {
        'page': models.ListingPage.get_solo(),
        'items': items,
    }

    return render(request, 'apps_listing_detail/listing.html', context)


def detail(request, pk, slug):
    item = get_object_or_404(models.Item.objects.published(for_user=request.user), pk=pk)

    if slug != item.get_slug():
        return redirect(item, permanent=True)

    context = {
        'item': item,
    }

    return render(request, 'apps_listing_detail/detail.html', context)
