from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Message, MessageHistory, Notification
from django.db.models.signals import post_save
# Define a custom signal for message creation

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    """
    Signal receiver that creates a notification when a new message is created.
    """
    if created:
        Notification.objects.create(
            user=instance.receiver,
            message=instance
        )

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:  # Only if this is an update
        old_message = Message.objects.get(pk=instance.pk)
        if old_message.content != instance.content:
            instance.edited = True
            instance.edited_at = timezone.now()
            MessageHistory.objects.create(
                message=old_message,
                old_content=old_message.content
            )