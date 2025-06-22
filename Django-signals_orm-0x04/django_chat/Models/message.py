from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    """ Model representing a chat message between users. """
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_chats')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)

    def __str__(self):
        return f"From {self.sender} to {self.receiver} at {self.timestamp}"
