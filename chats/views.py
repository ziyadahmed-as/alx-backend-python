from django.shortcuts import render
from rest_framework import viewsets, status  # status added from Django REST Framework
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # Added IsAuthenticated
from django_filters import rest_framework as filters  # filters added from built-in django_filters

from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from .permissions import IsParticipantOfConversation  # optional if using custom permission
from .pagination import MessagePagination  # Add pagination class
from .filters import MessageFilter  # Import the custom filter class


# Enhanced filter class for Message filtering (add sender, receiver, date filtering)
class MessageFilter(filters.FilterSet):
    conversation_id = filters.UUIDFilter(field_name="conversation__id")
    sender = filters.NumberFilter(field_name="sender__id")
    receiver = filters.NumberFilter(field_name="receiver__id")
    created_at_after = filters.DateTimeFilter(field_name="created_at", lookup_expr='gte')
    created_at_before = filters.DateTimeFilter(field_name="created_at", lookup_expr='lte')

    class Meta:
        model = Message
        fields = ['conversation_id', 'sender', 'receiver', 'created_at_after', 'created_at_before']


# ViewSets define the view behavior for the Conversation model
class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]  # Require authentication


# ViewSet handles CRUD for the Message model with filtering and pagination
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [filters.DjangoFilterBackend]  # enables filtering
    filterset_class = MessageFilter  # use custom filter set
    permission_classes = [IsAuthenticated]  # Require authentication
    pagination_class = MessagePagination  # Enable pagination (20 per page)

    def create(self, request, *args, **kwargs):
        if not request.data.get("message_body"):
            return Response(
                {"error": "Message body is required."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        conversation_id = request.data.get("conversation")
        if conversation_id:
            #  Filter and check if user is part of the conversation
            messages = Message.objects.filter(conversation_id=conversation_id)
            if not messages.filter(sender=request.user).exists() and not messages.filter(receiver=request.user).exists():
                return Response(
                    {"error": "You are not a participant of this conversation."},
                    status=status.HTTP_403_FORBIDDEN  #  Forbidden response
                )

        return super().create(request, *args, **kwargs)
