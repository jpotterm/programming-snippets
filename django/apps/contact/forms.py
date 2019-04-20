from django import forms
from dwaiter_form.core.forms import HoneypotField


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    bodyphoneemail = HoneypotField(required=False)
