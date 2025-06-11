from django.db import models
from django.contrib.auth.models import User

# Create a Message model with fields like sender, receiver, content, and timestamp.
class Message(models.Model):
    sender = models.ForeignKey('User', related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey('User', related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username} at {self.timestamp}"
    
# Create a Notification model to store notifications related to messages.

class Notification(models.Model):
    user = models.ForeignKey('auth.User', related_name='notifications', on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name='notifications', on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username} regarding message from {self.message.sender.username} at {self.timestamp}"   
    
