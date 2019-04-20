from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Notification)
def handle_notification_save(sender, instance, created, raw, **kwargs):
    if created and not raw:
        UserProfile.objects.create(user=instance)
