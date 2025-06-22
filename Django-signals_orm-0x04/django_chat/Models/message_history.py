from django.db import models
from .message import Message

class MessageHistory(models.Model):
    """ Model representing the history of edits made to a message. """
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='history')
    old_content = models.TextField()
    edited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History for Message {self.message.id} at {self.edited_at}"
