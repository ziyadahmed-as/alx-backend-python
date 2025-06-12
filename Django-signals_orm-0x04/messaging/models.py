from django.db import models
from django.contrib.auth.models import User
from .managers import UnreadMessagesManager  # Ensure this file exists

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)

    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    # Edit tracking
    edited = models.BooleanField(default=False)
    edited_at = models.DateTimeField(null=True, blank=True)
    edited_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='edited_messages')

    # Threading support
    parent_message = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    # Read/unread status
    read = models.BooleanField(default=False)

    # Managers
    objects = models.Manager()  # default manager
    unread = UnreadMessagesManager()  # custom unread manager

    def __str__(self):
        return f"From {self.sender.username} to {self.recipient.username}: {self.content[:20]}"

class MessageHistory(models.Model):
    message = models.ForeignKey(Message, related_name='history', on_delete=models.CASCADE)
    old_content = models.TextField()
    changed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History of Message ID {self.message.id}"
# Create a Notification model to store notifications related to messages.

class Notification(models.Model):
    user = models.ForeignKey('auth.User', related_name='notifications', on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name='notifications', on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username} regarding message from {self.message.sender.username} at {self.timestamp}"   
    
