import sys, os, django
sys.path.insert(0, '/')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vagrant.settings')
django.setup()

from django.utils import timezone
from django.contrib.auth.models import User
from apps.blog.models import BlogEntry, BlogEntryCategory
from apps.drop_off.models import DropOffLocation


def generate_blog():
    c = BlogEntryCategory()
    c.title = 'Category 1'
    c.color = '#FFFFFF'
    c.save()

    u = User.objects.get(pk=1)
    now = timezone.now()

    BlogEntry.objects.all().delete()

    for i in range(1000):
        year = 2000 + i // 8
        month = 1 + ((i // 2) % 12)
        entry = BlogEntry.objects.create(
            title='Post {}'.format(i),
            slug='post-{}'.format(i),
            content='<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>',
            author=u,
            publication_status=1,
            publication_date=now.replace(year=year, month=month)
        )
        entry.category.add(1)


def generate_drop():
    DropOffLocation.objects.all().delete()

    for i in range(30):
        d = DropOffLocation()
        d.name = 'Test {}'.format(i)
        d.address = '45 East Ave, Rochester, NY 14604'
        d.phone = '123-456-7890'

        d.clean()
        d.save()


generate_blog()
generate_drop()
