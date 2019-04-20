import os

from django.conf import settings
from django.db import models
from dwaiter_form.image.models import ImagePreviewField

from .content_item import ContentItem


class Image(ContentItem):
    image = ImagePreviewField(upload_to='apps/fluent_plugins/image')

    polymorphic_template = 'apps_fluent_plugins/image.html'
    polymorphic_icon = 'apps_fluent_plugins/images/image.png'
    polymorphic_description = 'Normal image'

    class Meta:
        app_label = 'apps_fluent_plugins'
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return os.path.basename(self.image.name) if self.image else ''
