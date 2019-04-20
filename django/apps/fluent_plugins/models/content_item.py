from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from polymorphic.models import PolymorphicModel


class ContentItem(PolymorphicModel):
    parent_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    parent_object_id = models.PositiveIntegerField()
    parent = GenericForeignKey('parent_content_type', 'parent_object_id')
    position = models.PositiveSmallIntegerField(null=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return ''
