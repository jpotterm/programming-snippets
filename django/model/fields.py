from apps.fluent_plugins.models import ContentItem
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils import timezone
from dwaiter_form.core.models import FileField, YoutubeUrlField
from dwaiter_form.image.models import ImageFocusCropField, ImagePreviewField
from dwaiter_form.rich_text.models import RichTextField


bool = models.BooleanField(default=False)
char = models.CharField(max_length=300)
email = models.EmailField(max_length=300)
file = FileField(upload_to='apps/general/example')
fluent_content = GenericRelation(ContentItem)
foreign_key = models.ForeignKey('User', on_delete=models.CASCADE, related_name='supervisors')
int = models.IntegerField()
many_to_many = models.ManyToManyField('User', blank=True, related_name='supervisors')
one_to_one = models.OneToOneField('User', on_delete=models.CASCADE, related_name='supervisor')
richtext = RichTextField()
text = models.TextField()
video = YoutubeUrlField()


# Image

image = models.ImageField(upload_to='apps/general/example')


# Preview (has meta orientation)

image = ImagePreviewField(
    'Image (optional)',
    upload_to='apps/post/post',
    help_text='Max size 10 MiB',
    validators=[MaxFileSizeValidator(10*1024*1024)],
)


# Focus crop

image = ImageFocusCropField(
    upload_to='apps/general/example',
    focus_x_field='image_focus_x',
    focus_y_field='image_focus_y',
)
image_focus_x = ImageFocusCropField.FloatField()
image_focus_y = ImageFocusCropField.FloatField()


# Choice

ICON_MONEY = 1
ICON_BOOK = 2
ICON_CHOICES = [
    (ICON_MONEY, 'Money'),
    (ICON_BOOK, 'Book'),
]
choices = models.IntegerField(choices=ICON_CHOICES)


# Need null=True
    ForeignKey
