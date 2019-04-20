from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from dwaiter.django.model_mixins import Displayable, MetaData
from dwaiter_form.image.models import ImageFocusCropField
from dwaiter_form.rich_text.models import RichTextField
from solo.models import SingletonModel


class ListingPage(MetaData, SingletonModel):
    class Meta:
        verbose_name_plural = 'Listing page'


class Item(Displayable):
    title = models.CharField(max_length=300)
    content = RichTextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'pk': self.pk,
            'slug': self.get_slug(),
        }
        return reverse('apps_listing_detail:detail', kwargs=kwargs)
