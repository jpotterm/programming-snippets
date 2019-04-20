from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse

from . import models


class BlogFeed(Feed):
    def get_object(self, request):
        return models.BlogListingPage.get_solo()

    def title(self, page):
        return page.meta_title

    def link(self, obj):
        return reverse('apps_blog:listing')

    def description(self, page):
        return page.meta_description

    def items(self):
        return models.Post.objects.published()[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.summary

    def item_pubdate(self, item):
        return item.publication_date

    def item_updateddate(self, item):
        return item.modification_date
