from django.contrib import admin
from grappelli.forms import GrappelliSortableHiddenMixin
from polymorphic.admin import GenericStackedPolymorphicInline

from . import models


class ContentItemInline(GrappelliSortableHiddenMixin, GenericStackedPolymorphicInline):
    class ImageInline(GrappelliSortableHiddenMixin, GenericStackedPolymorphicInline.Child):
        model = models.Image
        ct_field = 'parent_content_type'
	ct_fk_field = 'parent_object_id'

    class TextInline(GrappelliSortableHiddenMixin, GenericStackedPolymorphicInline.Child):
        model = models.Text
        ct_field = 'parent_content_type'
	ct_fk_field = 'parent_object_id'


    ct_field = 'parent_content_type'
    ct_fk_field = 'parent_object_id'
    model = models.ContentItem
    child_inlines = [
        ImageInline,
        TextInline,
    ]
