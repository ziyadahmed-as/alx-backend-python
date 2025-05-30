from django.shortcuts import render
from rest_framework import viewsets
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer  

# ViewSets define the view behavior for the Conversation and Message models
class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

# This viewset handles the CRUD operations for the Message model
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # Optionally, you can filter messages by conversation