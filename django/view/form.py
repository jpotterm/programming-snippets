def create_and_process_form(request, form_class, initial=None):
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)

        if form.is_valid():
            return (form, True)
    else:
        form = form_class(initial=initial)

    return (form, False)

def contact_view(request):
    form, processed = util.create_and_process_form(request, ContactForm)

    context = {
        'form': form,
    }

    if processed:
        form.save()
        return redirect('.')
    else:
        return render(request, 'contact.html', context)
