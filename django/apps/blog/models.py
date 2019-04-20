from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from dwaiter.django.model_mixins import Displayable, MetaData
from dwaiter_form.image.models import ImageFocusCropField
from dwaiter_form.rich_text.models import RichTextField
from solo.models import SingletonModel


class BlogListingPage(MetaData, SingletonModel):
    class Meta:
        verbose_name_plural = 'Blog listing page'


class Category(models.Model):
    title = models.CharField('title', max_length=300)

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Post(Displayable):
    title = models.CharField(max_length=300)
    category = models.ForeignKey('Category')
    summary = models.TextField()
    content = RichTextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'pk': self.pk,
            'slug': self.get_slug(),
        }
        return reverse('apps_blog:detail', kwargs=kwargs)
