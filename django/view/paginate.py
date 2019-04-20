from dwaiter.django.utils import paginate


def view(request):
    users = paginate(User.objects.all(), request.GET.get('page', 1), 10)
