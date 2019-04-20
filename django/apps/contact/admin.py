from django.contrib import admin
from dwaiter.django.admin import MetaDataAdmin
from solo.admin import SingletonModelAdmin

from . import models


@admin.register(models.ContactPage)
class ContactPageAdmin(SingletonModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'form_recipients',
            ],
        }),
    ] + MetaDataAdmin.fieldsets
