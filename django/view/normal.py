from django.shortcuts import render

def normal_view(request):
    context = {
        'one': 1,
    }

    return render(request, 'normal.html', context)
