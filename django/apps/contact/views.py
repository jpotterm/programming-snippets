from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from dwaiter.django.email import form_to_plaintext

from . import forms, models


def contact(request):
    page = models.ContactPage.get_solo()

    if request.method == 'POST':
        form = forms.ContactForm(request.POST)

        if form.is_valid():
            email_contact(form, page)
            messages.success(request, 'Thank you for your submission!')
            return redirect('.')
    else:
        form = forms.ContactForm()

    context = {
        'page': page,
        'form': form,
    }

    return render(request, 'apps_contact/contact.html', context)


# Helper functions


def email_contact(form, page):
    recipient_list = parse_csv_value(page.form_recipients)
    message = loader.get_template('apps_contact/email.txt').render(form.cleaned_data)
    html_message = loader.get_template('apps_contact/email.html').render(form.cleaned_data)

    send_mail(
        subject='{} Contact Submission'.format(settings.DWAITER_ACCOUNT_EMAIL_PREFIX_SUBJECT),
        message=message,
        html_message=html_message,
        from_email=form.cleaned_data['email'],
        recipient_list=recipient_list
    )


def parse_csv_value(value):
    return [x.strip() for x in value.split(',')]
