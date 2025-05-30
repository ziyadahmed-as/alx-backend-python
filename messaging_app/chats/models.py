from django.db import models
from django.contrib.auth.models import AbstractUser

# messaging_app/messaging_app/chats/models.py location of mymodels 
class User(AbstractUser):
    pass  # Extend with additional fields if needed

#define the Conversation models for the chats app  
class Conversation(models.Model):
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# this is the Message Model to store messages in the chats app
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)