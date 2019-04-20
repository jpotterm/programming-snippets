from django.db import models
from dwaiter.django.model_mixins import MetaData
from solo.models import SingletonModel


class ContactPage(MetaData, SingletonModel):
    form_recipients = models.TextField(help_text='Comma separated list of email addresses')

    class Meta:
        verbose_name_plural = 'Contact page'
