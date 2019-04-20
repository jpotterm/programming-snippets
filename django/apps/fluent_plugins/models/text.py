from django.db import models
from django.template.defaultfilters import striptags, truncatechars
from dwaiter_form.rich_text.models import RichTextField

from .content_item import ContentItem


class Text(ContentItem):
    content = RichTextField()

    polymorphic_template = 'apps_fluent_plugins/text.html'
    polymorphic_icon = 'apps_fluent_plugins/images/text.png'
    polymorphic_description = 'Title, subtitle, and paragraph'

    class Meta:
        app_label = 'apps_fluent_plugins'
        verbose_name = 'Text'
        verbose_name_plural = 'Text items'

    def __str__(self):
        return truncatechars(striptags(self.content), 50)
