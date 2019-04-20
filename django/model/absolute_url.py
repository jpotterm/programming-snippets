# Regular
    from django.core.urlresolvers import reverse

    def get_absolute_url(self):
        return reverse('apps_work:detail', kwargs={'pk': self.pk})

# Soft slug
    from django.template.defaultfilters import slugify
    from django.core.urlresolvers import reverse

    def get_absolute_url(self):
        kwargs = {
            'pk': self.pk,
            'slug': self.get_slug(),
        }
        return reverse('apps_work:detail', kwargs=kwargs)
