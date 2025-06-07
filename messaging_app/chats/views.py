from django.shortcuts import render
from rest_framework import viewsets, status  #  status added status method from DJango REST Framework
from rest_framework.response import Response
from django_filters import rest_framework as filters  # filters added from biult in django_filters

from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


# Optional: Custom filter class for Message filtering
class MessageFilter(filters.FilterSet):
    conversation_id = filters.UUIDFilter(field_name="conversation__id")

    class Meta:
        model = Message
        fields = ['conversation_id']


# ViewSets define the view behavior for the Conversation model
class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer


# ViewSet handles CRUD for the Message model with filtering
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [filters.DjangoFilterBackend]  # ✅ enables filtering
    filterset_class = MessageFilter  # ✅ use custom filter set

    def create(self, request, *args, **kwargs):
        if not request.data.get("message_body"):
            return Response(
                {"error": "Message body is required."},
                status=status.HTTP_400_BAD_REQUEST  # ✅ using status here
            )
        return super().create(request, *args, **kwargs)
